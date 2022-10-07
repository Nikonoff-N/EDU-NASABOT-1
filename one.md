1. Мы будем запрашивать данные с серверов NASA. ДЛя этоо нам понадобится скрипт на Python. Создайте файл one.py
2. Для работы с API нам надо делать http-запросы. обычно используют requests (почитайте самостоятельно об этой библиотеке). Но мы используем библиотеку httpx.
```
import httpx
```
3. Так же нам нужен ключ доступа(он же токен). К счатью для вас ,вы можете использовать мой. Но советую всё же сгенерировать свой по адрессу https://api.nasa.gov/.
Колличество запров в день ограничено, так что ваш токен будет лучше работать. Токен лежит в файле key.txt. Давайте откроем его, считаем и закинем в переменную. Не забудьте закрыть файл
```
f = open("key.txt") #открыли файл,теперь он в переменной
KEY = f.readline() # считали первую строчку
f.close() # закрыли файл
```
4. Итак, ключ в переменной пора делать запрос! На запрос поступит ответ,не забудьте записать его в переменную
```
r = httpx.get(f"https://api.nasa.gov/planetary/apod?api_key={KEY}") # Отправили запрос с нашим ключом и получили ответ
```
5. Это просто куча текста, мы бы не хотели заниматься его разбором, так что приобразуем его в словарь. Это супер удобная штука сформирует наши данные в пары ключ-значение.Подробнее в след. пункте.
```
data = r.json() #Переделали ответ в удобную форму словаря и записали в переменную
```
6. Теперь все наши данные в словаре и мы можем взять интересные нам. Вот все ключи словаря:copyright,date,hdurl,media_type,service_version,title,url
```
athor = data['copyright'] # по ключу copyright нашли автора
exp = data['explanation'] #по ключу explanation нашли описание
title = data['title'] #по ключу title нашли заголовок
image = data['url'] #по ключу url нашли изображение(адрес  в интернете)
```
7. Не забудем вывести данные в консоль
```
print(athor)
print(title)
print(image)
print(exp)
```
8. Что бы посмотреть картинку, нажмите на её адресс в консоли.
9. 
10. 