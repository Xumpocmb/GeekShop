# Geek Shop

---

## Clothes Shop for Geeks

### :warning: !! work in progress !! :warning:

---
# Задача проекта:
* Создать интернет магазин одежды.

## :information_source: Возможности:
* Просмотр каталога одежды.

* Регистрация пользователя.

* Личный кабинет пользователя.

* Корзина покупок пользователя.

---

# Dev notes:

## Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

## Install and setup:
```
pip install django
django-admin startproject GeekShop
```

## create app:
```
python manage.py startapp products
```

## Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

## Super User
```
python manage.py createsuperuser
```


setup static:
```
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

---


