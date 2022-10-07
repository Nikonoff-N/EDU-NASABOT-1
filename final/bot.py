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
    update.message.reply_text(f'Привет,{user.first_name}!\n /help - список комманд \n /about - о создателе \n /today - фото дня \n /random - случайное фото')



def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('/help - список комманд \n /about - о создателе /today - фото дня \n /random - случайное фото')

def about_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Никонов Дмитрий\nЦТТ АргТех\nБоровичи, 2022')

def today_nasa(update: Update, context: CallbackContext) -> None:
    r = httpx.get(f"https://api.nasa.gov/planetary/apod?api_key={KEY}") # Отправили запрос с нашим ключом и получили ответ
    data = r.json() #Переделали ответ в удобную форму словаря и записали в переменную
    athor = data['copyright'] # по ключу copyright нашли автора
    exp = data['explanation'] #по ключу explanation нашли описание
    title = data['title'] #по ключу title нашли заголовок
    image = data['url'] #по ключу url нашли изображение(адрес  в интернете)

    update.message.reply_text(f'Автор:{athor}\nНазвание:{title}\nОписание:{exp}')
    update.message.reply_photo(image)

def random_nasa(update: Update, context: CallbackContext) -> None:
    r = httpx.get(f"https://api.nasa.gov/planetary/apod?api_key={KEY}&count=1") # Отправили запрос с нашим ключом и получили ответ
    data = r.json() #Переделали ответ в удобную форму словаря и записали в переменную
    data = data[0] #Из ответа нам нужен только первое фото
    athor = data['copyright'] # по ключу copyright нашли автора
    exp = data['explanation'] #по ключу explanation нашли описание
    title = data['title'] #по ключу title нашли заголовок
    image = data['url'] #по ключу url нашли изображение(адрес  в интернете)
    update.message.reply_text(f'Автор:{athor}\nНазвание:{title}\nОписание:{exp}')
    update.message.reply_photo(image)

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

    dispatcher.add_handler(CommandHandler("today", today_nasa))
    dispatcher.add_handler(CommandHandler("random", random_nasa))
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