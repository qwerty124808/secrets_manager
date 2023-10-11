## api для создания и просмотра одноразовых секретов

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

### Технологии:
- python 3.7
- fastapi 0.103.1
- Mongo DB
- pymongo
- Docker
- Docker-compose
- pydantic
- pytest
- pycrypto

### Инструкция для развертывания проекта с использованием Docker:

Клонирование проекта:
```
git clone https://github.com/qwerty124808/secrets_manager
```
Запуск:

Для запуска проекта необходимо создать окружение командой
```
pipenv shell
```

Запустить команду, указанную ниже из корня проекта 
```
sudo docker-compose up -d
```

Пример использования:

1. Заходим в postman
3. Создаем секрет
4. Отправляем POST запрос на эндпоинт - чтобы получить ссылку на наш секрет:
```
http://127.0.0.1:8000/generate
```

Тело запроса должно быть в формате Json и выглядеть примерно так:
```
{
    "secret": "Ваш секрет",
    "password": "Ваш пароль"
}
```
Далее переходим по ссылке которую мы получили 

Отправляем POST запрос для получения содержания секрета на эндпоинт:
```
http://localhost/secret/<id-секрета>
```
Body в запросе должно быть в формате Json и выглядеть вот так:
```
{
    "password": "Ваш пароль"
}
```
Посмотреть все реализованные эндпоинты можно по адресу:
```
http://127.0.0.1:8000/docs
```

Автор проекта Дмитрий Алтарев