from telegram import ChatAction,InlineQueryResultArticle,InlineQueryResultPhoto, ParseMode, InputTextMessageContent, Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler,Updater, InlineQueryHandler, CommandHandler, CallbackContext,MessageHandler,Filters
from telegram.utils.helpers import escape_markdown

def sendHtml(update,html):
    return update.message.reply_text(html, parse_mode=ParseMode.HTML)

def editHtml(message,html):
    return message.edit_text(html, parse_mode=ParseMode.HTML)

def mensajes(update,context):
    username = update.message.chat.username
    msg = update.message.text
    name = str(msg).split(' ')[1].split('.1.')[2].split('.2.')[3].split('.3.')[4].split('.4.')[5].split('.5.')[6].split('.6.')
    nombre = name[0]
    episodio = name[1]
    youtuber = name[2]
    calidad = name[3]
    partes = name[4]
    peso = name[5]
    link = name[6]

    if '/test' in msg:
        sendHtml(update,'Congratulations!')
    elif '/p' in msg:
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