from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction

# Database and token 
import os
from Resources import Conector_Students as conector 
db = conector.database(os.getenv('MONGO'))


# Date
from datetime import datetime

# Open AI
from Resources import ChatGPT

#Commands
def start(update, context):
    """Saluda a hikari"""
    from Resources.SimpleFunctions import send_saludo as saludo 
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=saludo())
    #Debug
    print('Comando ejecutado: start')

def help(update, context):
    """ Acerca de Hikari Bot"""
    from Resources.SimpleFunctions import help
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)
    if update.message.from_user.first_name == 'Hola. Al3x': # I'm admin
        from Resources.SimpleFunctions import help_admin
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_admin)
        print('Comando ejecutado: help admin')
    print('Comando ejecutado: help')

def rules(update, context):
    """Reglas de la comunidad AprenderPython"""
    from Resources.SimpleFunctions import rules
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rules)
    print('Comando ejecutado: rules')

def quees(update, context):
    """Busqueda de definiciones"""
    from Resources.SimpleFunctions import definiciones
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_say = " ".join(context.args)
    answer = definiciones(user_say)
    update.message.reply_text(answer)   
    print("/quees", user_say)


# Here beign a Students functions
def list_students(update, context):
    """Enlistar alumnos"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    answer=list(map(lambda x: (f'''{x['_id']}, {x['name']}'''), db.view_students()))
    try:
        student_id= int("".join(context.args))
        answer =  list(map(lambda x:x, db.view_student_specific(student_id)))[0]
        info = f'''
ID : {answer['_id']}
Nombre: {answer['name']}
Reclamos: {answer['claims']}
Veces que ha limpiado: {answer['times_clean']}
Última limpieza: {answer['last_time']}
            '''
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(info))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print("/list", answer)

def insert_student(update, context):
    """Insertar alumno"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = (" ".join(context.args)).split(",")
    answer = db.insert_student(insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=(str(answer)))
    print('/insert', answer)
 

def update_student(update, context):
    """Actualizar alumno"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = (" ".join(context.args)).split(",")
    setup = '''
ID
Nombre
Reclamos
Veces que se limpio
Última vez que limpio
    '''
    answer = db.update_student(insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=(setup, str(answer)))
    print('/update', insert)


def delete_student(update, context):
    """Insertar alumno"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = int(" ".join(context.args))
    answer = db.delete_student(insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print('/delete', insert)

def confirm(update, context):
    """Confirmar limpieza"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = int(" ".join(context.args))
    # Date and counter
    times = list(map(lambda x:(
        x['_id'],
        x['times_clean']
    ), db.view_student_specific(insert)))[0]

    answer = db.confirm([
        insert, # ID 
        (times[1]+1),# Times clean
        str(datetime.now())
    ])

    longitud = list(map(lambda x:x, db.view_students()))
    if insert >= 1 and insert < len(longitud):
        student = insert+1
    else:
        student = 1
        
    out = list(map(lambda x:x, db.view_student_specific(student)))[0]
    out = out['_id'], out['name']


    answer = f'''
{answer}, 
Siguiente estudiante: {out[0]}: {out[1]}
    '''

    context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print('/confirm', insert, answer)

def chat_gpt(update, context):
    """Usa GPT-3 para resolver tus dudas"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = (" ".join(context.args))
    answer = ChatGPT.chatgpt(os.getenv("OPENAI_TOKEN"), insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print('/gpt', insert)

#Start TelBot 
token = os.getenv("TELEGRAM_TOKEN") 
updater = Updater(token=token, use_context=True)

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)
quees_handler = CommandHandler("quees", quees)
list_students_handler = CommandHandler("list", list_students)
insert_student_handler = CommandHandler("insert", insert_student)
update_student_handler = CommandHandler("update", update_student)
delete_student_handler = CommandHandler("delete", delete_student)
confirm_handler = CommandHandler("confirm", confirm)
chat_gpt_handler = CommandHandler("gpt", chat_gpt)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)
updater.dispatcher.add_handler(quees_handler)
updater.dispatcher.add_handler(list_students_handler)
updater.dispatcher.add_handler(insert_student_handler)
updater.dispatcher.add_handler(update_student_handler)
updater.dispatcher.add_handler(delete_student_handler)
updater.dispatcher.add_handler(confirm_handler)
updater.dispatcher.add_handler(chat_gpt_handler)

updater.start_polling()
