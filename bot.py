from telegram import Update, bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

"""
{'username': 'krpajay', 'is_bot': False, 'last_name': 'K', 'first_name': 'Ajay', 'language_code': 'en', 'id': 1996882591}
"""


def bookinfo(update, context: CallbackContext):
    update.message.reply_text(text='What book are you looking for?🔎')


def get_bookinfo(update, context: CallbackContext):
    book_name = update.message.text
    book_name = str.lower(book_name)
    # TODO: do what you want with book name

    answer = f'You have wrote me {book_name}'
    update.message.reply_text(answer)


def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5118867823:AAGUA2RZJKtu0wztFcOS05_6WnECsph53fs')

updater.dispatcher.add_handler(CommandHandler('hello', ping))
updater.dispatcher.add_handler(CommandHandler('bookinfo', bookinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.text, get_bookinfo))
updater.start_polling()
updater.idle()

# Next Idea - YouTube Downloader
