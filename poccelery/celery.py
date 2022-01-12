import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poccelery.settings")

app = Celery("poccelery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.task_ignore_result = True  # TO COMMENT IF WANT RESULT IN REDIS


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
