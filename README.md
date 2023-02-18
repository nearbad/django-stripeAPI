# django-stripeAPI

## Функционал
Проект реализует следующие Django + Stripe API бэкенд со следующим функционалом

- Создание модели Item с полями (name, description, price)
- Получение Stripe Session Id для оплаты выбранного Item с помощью API метода GET /buy/{id}
- Получение HTML страницы с информацией о выбранном Item и кнопкой Buy с помощью API метода GET /item/{id}
- Объединение нескольких Item в модель Order и совершение платежа на содержимое Order
- Добавление моделей Discount и Tax, которые можно прикрепить к модели Order
- Использование environment variables для безопасности Stripe API ключей

## Как использовать
1. Установите зависимости, используя команду `pip install -r requirements.txt`.
2. Создайте файл `.env` и добавьте свои Stripe API ключи в переменные `STRIPE_PUBLISHABLE_KEY` и `STRIPE_SECRET_KEY`.
3. Запустите миграции, используя команду `python manage.py migrate`.
4. Создайте superuser с помощью команды `python manage.py createsuperuser`
5. Создайте Item через админ панель перейдя на страницу `http://localhost:8000/admin`
6. Запустите проект, используя команду `python manage.py runserver`.
7. Откройте браузер и перейдите на страницу `http://localhost:8000/item/{item_id}` для покупки Item.

## Как запустить с помощью Docker
1. Склонируйте репозиторий: `git clone https://github.com/nearbad/django-stripeAPI`.
2. Перейдите в директорию проекта: `cd django-stripeAPI`.
3. Создайте файл `.env` и добавьте свои Stripe API ключи в переменные `STRIPE_PUBLISHABLE_KEY` и `STRIPE_SECRET_KEY`.
4. Соберите образ Docker: `docker build -t django-stripeapi ..`
5. Запустите контейнер: `docker run -p 8000:8000 -d django-stripeapi`.
6. Откройте браузер и перейдите на страницу `http://localhost:8000/item/{item_id}` для покупки Item.
