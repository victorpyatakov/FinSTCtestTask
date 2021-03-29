# Тестовое задание FinSTC Software LLC 

## Задание:
1. Создать небольшое REST API на Python (можно использовать любые библиотеки и framework-и, в т.ч. Flask).
2. Требуется создание только бэкэнд части, в readme файле желательно описать endpoint и примеры запросов (будет плюсом наличие файлов-схем запросов, например JSON Schema).
3. Данное API должно поддерживать CRUD операции.
4. Тематика данного API связана с продажами машин автодилерами. Модель данных (в т.ч. описание и взаимодействие между классами "Машина" и "Дилер") можете разработать любую, на ваше усмотрение, но соответствующую условиям выше.  

## Запуск:
* активировать виртуальную среду
```shell script
virtualenv venv 
source venv/bin/activate
```
* установить пакеты из файла requirements.txt
```shell script
pip install -r requirements.txt
```
*  сделать миграции в базе данных
```shell script
python manage.py migrate
```
* создать супер пользователя
```shell script
python manage.py createsuperuser
```
* запусить сервер
```shell script
python manage.py runserver
```
      
## Описание url:
* admin/ - админка джанго
* api/v1/ - апи для crud 
* swagger/  - описание апи свагер
* redoc/ - описание апи документация

## Работа с апи:
### для CRUD операций с диллером, используется:
* endpoint: api/v1/dealer/
* методы: GET, POST
* JSON:
```shell script
{
    "name": "Audi",
    "city": "Berlin"
}
```
*  endpoint: api/v1/dealer/<pk>
*  методы: GET, PUT, PATCH, DELETE
*  JSON:
```shell script
{
    "name": "Audi",
    "city": "Berlin"
}
```
### для CRUD операций с машиной, используется:
* endpoint: api/v1/car/
* методы: GET, POST
* JSON:
```shell script
{
    "dealer_id": 1,
    "name": "A1",
    "price": "2800.99",
    "color": "Black"
}
```
* endpoint: api/v1/car/<pk>
* методы: GET, PUT, PATCH, DELETE
* JSON:
```shell script
{
    "dealer_id": 1,
    "name": "A1",
    "price": "2800.99",
    "color": "Black"
}
```
#### Более подробно можно посмотреть в /swagger/ или  /redoc/.
    
    
