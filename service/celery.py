import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

app = Celery("service")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.timezone = "Europe/Moscow"
