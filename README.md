# Product Management Application

Это небольшое Django-приложение для управления продуктами. Оно предоставляет API для создания и получения списка продуктов, а также HTML-страницу для взаимодействия с этим API.

## Установка

1. Клонируйте репозиторий:

_bash_

`git clone git@github.com:lets-dancing/test_for_interview_Brendwall.git`

`cd product_project`


2. Создайте и активируйте виртуальное окружение:

_bash_

`python -m venv venv`

`source venv/bin/activate`

***Для Windows используйте***
`venv\Scripts\activate`


3. Установите зависимости:

_bash_

`pip install -r requirements.txt`


4. Примените миграции для настройки базы данных:

_bash_

`python manage.py migrate`


5. Запустите сервер разработки:

_bash_

`python manage.py runserver`


6. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/` для доступа к приложению.

## API

### Создание продукта

- **URL:** `/api/products/`
- **Метод:** `POST`
- **Формат данных:** JSON
- **Параметры:**
  - `name` (string): Название продукта (обязательное поле)
  - `description` (string): Описание продукта (обязательное поле)
  - `price` (decimal): Цена продукта (должна быть положительным числом)

### Получение списка продуктов

- **URL:** `/api/products/`
- **Метод:** `GET`
- **Формат ответа:** JSON

## Фронтенд

HTML-страница предоставляет форму для добавления нового продукта и таблицу для отображения всех существующих продуктов. Данные отправляются и запрашиваются с помощью Fetch API.

## Используемые технологии

- Django
- Django REST Framework
- SQLite (по умолчанию в Django)
- HTML и JavaScript
