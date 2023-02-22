from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction

# Database 
from Resources import Conector_Students as conector 

db = conector.database()

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
    #Debub
    print('Comando ejecutado: help')

def rules(update, context):
    """Reglas de la comunidad AprenderPython"""
    from Resources.SimpleFunctions import rules
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rules)
    print('Comando ejecutado: rules')

def list_students(update, context):
    """Enlistar alumnos"""
    answer = db.view_students()
    info = []
    for data in answer:
        text = f'{data["name"]}: {data["_id"]}'
        info.append(text)

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(info))
    print(info)


def list_student_specific(update, context):
    """Enlistar alumno especifico"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    student_id= int(" ".join(context.args))
    answer =  db.view_student_specific(student_id)
    for data in answer:
        info = f'''
ID : {data['_id']}
Nombre: {data['name']}
Usuario: {data['user']}
Reclamos: {data['claims']}
Veces que ha limpiado: {data['times_clean']}
            '''
        # update.message.reply_text(answer)   
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(info))
        print('/list_st', info)

def insert_student(update, context):
    """Insertar alumno"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = (" ".join(context.args)).split(",")
    answer = db.insert_student(insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print('/insert', insert)

def delete_student(update, context):
    """Insertar alumno"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    insert = int(" ".join(context.args))
    answer = db.delete_student(insert)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(answer))
    print('/delete', insert)

#Start TelBot 
token ='5720318591:AAE_CEfcSwvL2zq1k-KC27iZhSnoGUNDvl'
updater = Updater(token=token, use_context=True)

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)
list_students_handler = CommandHandler("list", list_students)
list_student_specific_handler = CommandHandler("list_st", list_student_specific)
insert_student_handler = CommandHandler("insert", insert_student)
delete_student_handler = CommandHandler("delete", delete_student)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)
updater.dispatcher.add_handler(list_students_handler)
updater.dispatcher.add_handler(list_student_specific_handler)
updater.dispatcher.add_handler(insert_student_handler)
updater.dispatcher.add_handler(delete_student_handler)

updater.start_polling()
