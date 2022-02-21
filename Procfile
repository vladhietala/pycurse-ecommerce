release: python3 manage.py migrate
release: python3 manage.py createsuperuser --noinput
web: gunicorn loja.wsgi --preload --log-file -
