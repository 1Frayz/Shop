# SushiLavka

"SushiLavka" - это веб-приложение для онлайн-магазина доставки еды, созданное на основе фреймворка Django. Проект включает в себя интеграцию с различными технологиями и инструментами для обеспечения функциональности интернет-магазина.

## Технологический стек

- **Django**: Основной фреймворк для создания веб-приложения, обеспечивающий управление данными, аутентификацию, роутинг и другие функции.
- **Redis**: Используется для сбора рекомендаций, представляя собой базу данных в памяти, полезную для реализации рекомендательных систем.
- **Celery**: Фреймворк для асинхронной обработки задач, используется для обработки заказов в фоновом режиме, что повышает эффективность работы приложения.
- **Платежная система Pikassa**: Интегрирована для обработки онлайн-платежей за заказы, обеспечивая удобный и безопасный платежный процесс.
- **PostgreSQL**: Используется в качестве реляционной базы данных для хранения информации о продуктах, заказах, пользователях и других данных, необходимых для функционирования интернет-магазина.

## Установка

Для установки и настройки проекта выполните следующие шаги:

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/sushilavka.git
    cd sushilavka
    ```

2. Установите зависимости с помощью `pip`:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте базу данных PostgreSQL в файле `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
        }
    }
    ```

4. Примените миграции:
    ```sh
    python manage.py migrate
    ```

5. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Настройки

Файл настроек `settings.py` содержит основные параметры конфигурации проекта:

- **BASE_DIR**: Базовый каталог проекта.
- **SECRET_KEY**: Секретный ключ для криптографических операций (должен быть скрыт в продакшене).
- **DEBUG**: Режим отладки (не включайте в продакшене).
- **ALLOWED_HOSTS**: Список хостов/доменов, для которых допустимы запросы к этому приложению.
- **INSTALLED_APPS**: Список установленных приложений Django.
- **MIDDLEWARE**: Список промежуточного ПО.
- **DATABASES**: Настройки базы данных.
- **AUTH_PASSWORD_VALIDATORS**: Валидаторы паролей.
- **LANGUAGE_CODE**: Язык интерфейса.
- **TIME_ZONE**: Часовой пояс.
- **STATIC_URL**: URL для статических файлов.
- **MEDIA_URL**: URL для медиа файлов.
- **CART_SESSION_ID**: Идентификатор сессии корзины.

## Использование Redis и Celery

Для использования Redis и Celery, убедитесь, что Redis запущен и доступен. Настройки Redis в `settings.py`:
```python
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
```

Запустите Celery worker:
```sh
celery -A sushilavka worker --loglevel=info
```

## Платежная система Pikassa

Для интеграции с платежной системой Pikassa, настройте API-ключи и URL:
```python
API_KEY = 'your_api_key'
SECRET_PHRASE = 'your_secret_phrase'
URL = 'https://pikassa.io/merchant-api/api/v2/invoices'
```

Если у вас возникли вопросы или предложения, пожалуйста, создайте issue или отправьте pull request. Мы рады любой помощи и сотрудничеству!
![Screenshot 2023-10-13 171517](https://github.com/1Frayz/Shop/assets/98277379/22324282-7f7b-4239-9fb9-e9a860baba7d)
![Screenshot 2023-10-13 171542](https://github.com/1Frayz/Shop/assets/98277379/92ca62cb-2063-4267-a5f5-4a859f57b90f)
![Screenshot 2023-10-13 171751](https://github.com/1Frayz/Shop/assets/98277379/2cc4d9db-e0de-4a81-9b85-5784361d411c)
![Screenshot 2023-10-13 171803](https://github.com/1Frayz/Shop/assets/98277379/5714e329-d6da-41f5-a3f8-417d2fbb2b81)
![Screenshot 2023-10-13 171817](https://github.com/1Frayz/Shop/assets/98277379/86122d95-1604-4c9e-a546-027b03f775d4)
![Screenshot 2023-10-13 172015](https://github.com/1Frayz/Shop/assets/98277379/2a6758bc-3931-4df9-b7ac-b022ad79fbda)
![Screenshot 2023-10-13 172044](https://github.com/1Frayz/Shop/assets/98277379/846a9d71-5522-4625-b80a-0b1f650220ef)


