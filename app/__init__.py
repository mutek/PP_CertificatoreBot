from telegram.ext import Updater
from .secret import secret_token

updater = Updater(secret_token, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

from telegram.ext import CommandHandler

def help_fun(update, context):
    topic = {
        "lince": "Lince non esiste, te lo sei immaginato.\n\nSul serio",
        "lqfb": "È troppo presto per parlarne, ma è un software che gestisce le mozioni politiche del partito."
    }

    argomento = update.message.text[6:] 
    if argomento in topic:
        risposta = topic[argomento]
    else:
        risposta = "Non ho capito. Gli argomenti disponibili sono {}".format(', '.join(topic))
        
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=risposta)

help_handler = CommandHandler('help', help_fun)

dispatcher.add_handler(help_handler)
