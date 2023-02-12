#Verion Beta
from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction

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

#Start Hikari
token = input('insert a token: ')
updater = Updater(token=token, use_context=True)

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)

updater.start_polling()
