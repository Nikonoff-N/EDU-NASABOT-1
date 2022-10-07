1. За основу возьмём стандартного бота. Подключим библиотеки и подтянем ключ к API NASA.
```
#Библиотеки для бота
import logging #Пишет логи, очень полезная штука

#Делают за нас всю работу
from telegram import Update, ForceReply,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,CallbackQueryHandler

import httpx

f = open("key.txt") #открыли файл,теперь он в переменной
KEY = f.readline() # считали первую строчку
f.close() # закрыли файл
```

2. Преобразуем программу one.py в комманду для бота
```
def today_nasa(update: Update, context: CallbackContext) -> None:
    r = httpx.get(f"https://api.nasa.gov/planetary/apod?api_key={KEY}") # Отправили запрос с нашим ключом и получили ответ
    data = r.json() #Переделали ответ в удобную форму словаря и записали в переменную
    athor = data['copyright'] # по ключу copyright нашли автора
    exp = data['explanation'] #по ключу explanation нашли описание
    title = data['title'] #по ключу title нашли заголовок
    image = data['url'] #по ключу url нашли изображение(адрес  в интернете)

    update.message.reply_text(f'Автор:{athor}\nНазвание:{title}\nОписание:{exp}')
    update.message.reply_photo(image)
```
3. Не забудем привязать функцию к команде в функции main.
```
    # По разным командам запускаем разные функции
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about_command))

    dispatcher.add_handler(CommandHandler("today", today_nasa))
```
4. Преобразуем программу two.py в комманду для бота
```
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
```
5. Не забудем привязать функцию к команде в функции main.
```
    # По разным командам запускаем разные функции
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about_command))

    dispatcher.add_handler(CommandHandler("today", today_nasa))
    dispatcher.add_handler(CommandHandler("random", random_nasa))
```