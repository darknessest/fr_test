# fr_test

Тестовое задание для Фабрики Решений

## Running

### Locally

To run it using django enter following command:

```shell
python manage.py runserver 0.0.0.0:8000
```

To run it using gunicorn enter following command:

```shell
gunicorn fabres.wsgi:application --bind 0.0.0.0:8000
```

check that `ALLOWED_HOSTS` in `fabres/settings.py` have a host that you want to use

### Docker

Run following comand to build production version of this project:

```shell
sudo chmod +x entrypoint.sh
docker-compose -f docker-compose.dev.yml up --build
```

or following for production

```shell
sudo chmod +x entrypoint.sh
docker-compose -f docker-compose.yml up --build
```

Checkout entrypoint.sh before using server, it creates admin and user for django.