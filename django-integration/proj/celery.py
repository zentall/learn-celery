import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("proj")

app.conf.beat_schedule = {
    "check-every-five-minutes-to-send-email-notifications": {
        "task": "polls.tasks.batch_task",
        "schedule": crontab(minute="*/1"),  # Every 1 minutes
    },
}

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
