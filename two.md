1. Что бы получить случайное изображение добавим параметр count к запросу
```
r = httpx.get(f"https://api.nasa.gov/planetary/apod?api_key={KEY}&count=1") # Отправили запрос с нашим ключом и получили ответ
```
2. Поскольку обычно данный запрос должен отправлять много картинок, он отправляет <b>список</b>. Нам нужен только перый элемент списка, нумерация списков начинается с нуля.
```
data = r.json() #Переделали ответ в удобную форму словаря и записали в переменную
data = data[0] #Из ответа нам нужен только первое фото
athor = data['copyright'] # по ключу copyright нашли автора
exp = data['explanation'] #по ключу explanation нашли описание
title = data['title'] #по ключу title нашли заголовок
image = data['url'] #по ключу url нашли изображение(адрес  в интернете)
```