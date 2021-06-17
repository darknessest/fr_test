#!/bin/sh
ls
python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py shell -c "from django.contrib.auth.models import User; import os;
User.objects.create_superuser('admin', 'a@b.co', os.environ.get('django_admin_pass','QarJEXZeHqsRQ3ko')).save();
User.objects.create_user('test_user', 'a@b.co', 'test_user_password').save();"


exec "$@"