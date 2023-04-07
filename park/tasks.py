from celery import shared_task
from django_celery_beat.models import crontab

from attendance.models import Student

@shared_task
def update_my_checkbox_field_task():
    Student.objects.update(attendance=True)
