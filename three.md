Дополним функционал бота новой командой и дублированием пользовательского сообщения.

1. Добавим новую функцию для отправки случайного эмодзи:
```
def randomEmoji(update: Update, context: CallbackContext) -> None:
    emojiList = ['😁','😂','😃','😄','😅','😍']
    myEmoji = random.choice(emojiList)
    update.message.reply_text(myEmoji)
```
Справка:
  `emojiList` представляет собой одномерный массив, а нумерация его элементов ВСЕГДА начинается с 0.
  
2. Не забываем о привязке функции к команде в перечне функции main:
```
# По разным командам запускаем разные функции
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about_command))
    
    dispatcher.add_handler(CommandHandler("randomEmoji", randomEmoji))
```
3. Добавим новую функцию на дублирование сообщения пользователя:
```
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
```
4. Не забываем о привязке данной функции в перечне функции main:
```
# По НЕ команде запускаем функцию эхо
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
```
Справка:
`Filters.text & ~Filters.command`- это параметры, означающие что функция `echo` будет выполняться при условии, что сообщение пользователя содержит текст и НЕ ЯВЛЯЕТСЯ командой.
