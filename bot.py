"""
Простой наса-бот для телеграмма
Сперва напишите функции обработки сообщений
Затем эти функции отправляются диспетчеру и регистрируются к соответствующим командам.
Затем бот запускается и работает пока вы не нажмёте Ctrl-C в консоли

Инструкция:
Просто наса-бот.Есть две комманды - фото дня и рандомное фото.
нажмите Ctrl-C консоли что бы остоновить бота
"""

#Библиотеки для бота
import logging #Пишет логи, очень полезная штука

#Делают за нас всю работу
from telegram import Update, ForceReply,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,CallbackQueryHandler

import httpx

f = open("key.txt") #открыли файл,теперь он в переменной
KEY = f.readline() # считали первую строчку
f.close() # закрыли файл

# Включаем логи
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(f'Привет,{user.first_name}!')



def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('/help - список комманд')

def about_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Никонов Дмитрий\nЦТТ АргТех\nБоровичи, 2022')



def main() -> None:
    """Запуск бота"""
    # Запускаем бота и передаём токен
    updater = Updater("TOKEN")

    # Создаём диспечера
    dispatcher = updater.dispatcher

    # По разным командам запускаем разные функции
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about_command))


    # По НЕ команде запускаем функцию эхо
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, help_command))

    # Запуск бота
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()