from telegram import ChatAction,InlineQueryResultArticle,InlineQueryResultPhoto, ParseMode, InputTextMessageContent, Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler,Updater, InlineQueryHandler, CommandHandler, CallbackContext,MessageHandler,Filters
from telegram.utils.helpers import escape_markdown

def sendHtml(update,html):
    return update.message.reply_text(html, parse_mode=ParseMode.HTML)
    
def sendMessage(update):
    return update.message.reply_text(update.message.chat.id)    
    
def editMessage(update):
    return update.message.edit_text(update.message.chat.id)    
    
def editHtml(message,html):
    return message.edit_text(html, parse_mode=ParseMode.HTML)

def mensajes(update,context):

    if '/start' in msg:
        sendMessage(update,'🔰TamplateBot iniciado con éxito🔰')
        return
    elif '/tamp' in msg:
    	try:
    		username = update.message.chat.username
    		msg = update.message.text
    		name = str(msg).split('')
    		capitulo = name[2]
    		nombre = name[1]
  		  youtuber = name[3]
   		 calidad = name[4]
   		 partes = name[5]
  		  peso = name[6]
   		 link = name[7]
   	 else:
   	 	infotext = f'✏️Nombre: {nombre}\n'
        infotext+= f'🎬Episodio: {episodio}\n'
        infotext+= f'🆔YouTuber: {youtuber}\n'
        infotext+= f'Calidad: {calidad}\n'
        infotext+= f'📦Partes: {partes}\n'
        infotext+= f'🏋️‍♂️Peso: {peso}\n'
        infotext+= '⏰Vence: 24h\n\n\n'
        infotext+= f'        <a href="{link}">📥 Descargar txt aquí 📥</a>\n\n\n'
        infotext+= '        ↘️⬇️⬇️⬇️⬇️⬇️⬇️↙️\n'
        infotext+= '        ➡️@YoutubeNube ⬅️\n'
        infotext+= '        ↗️⬆️⬆️⬆️⬆️⬆️⬆️⬆️\n\n'
        infotext+= '   💎Resubida solo por VIP💎\n'
        infotext+= '               @Danny5367'
        sendHtml(update,infotext)
        except:
        	sendMessage(update, 'Hubo un error al crear la plantilla, vuelva a intentarlo')
        return	

def main() -> None:
    try:
        updater = Updater('5323660513:AAFA-B2sOj5QQQ8SyQPI9wz4WpeyCUDMrBU')
        dispatcher = updater.dispatcher
        dispatcher.add_handler(MessageHandler(Filters.text,mensajes))
        updater.start_polling()
        updater.idle()
    except Exception as ex:
        print(str(ex))
        main()

if __name__ == '__main__':
    main()
