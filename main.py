from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction

# Database and token 
from Resources import token
from Resources import Conector_Students as conector 
db = conector.database()

# Date
from datetime import datetime

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

# Here beign a Students functions
def list_students(update, context):
    """Enlistar alumnos"""
    answer=list(map(lambda x: (f'''{x['_id']}, {x['name']}'''), db.view_students()))
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    try:
        student_id= int("".join(context.args))
        answer =  list(map(lambda x:x, db.view_student_specific(student_id)))
        answer = answer[0]
        info = f'''
ID : {answer['_id']}
Nombre: {answer['name']}
Usuario: {answer['user']}
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
    answer = db.update_student(insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=(str(answer)))
    print('/insert', answer)
 

def update_student(update, context):
    """Actualizar alumno"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = (" ".join(context.args)).split(",")
    setup = '''
ID
Nombre
Usuario
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
        x['times_clean']
    ), db.view_student_specific(insert)))
    information = [
        insert, # ID 
        (times[0]+1),# Times clean
        str(datetime.now())
    ]
    print(information)
    answer = db.confirm(information)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print('/confirm', insert, information)



#Start TelBot 
token = token.token_tel() 
updater = Updater(token=token, use_context=True)

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)
list_students_handler = CommandHandler("list", list_students)
insert_student_handler = CommandHandler("insert", insert_student)
update_student_handler = CommandHandler("update", update_student)
delete_student_handler = CommandHandler("delete", delete_student)
confirm_handler = CommandHandler("confirm", confirm)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)
updater.dispatcher.add_handler(list_students_handler)
updater.dispatcher.add_handler(insert_student_handler)
updater.dispatcher.add_handler(update_student_handler)
updater.dispatcher.add_handler(delete_student_handler)
updater.dispatcher.add_handler(confirm_handler)

updater.start_polling()
