from __future__ import absolute_import, unicode_literals
from datetime import datetime
# from celery.task import task
from celery import shared_task
from celery.app.base import app_has_custom
from django.http.response import HttpResponse 
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
from django.apps import apps

app = Celery('tasks',broker="redis://localhost:6379/0")
from apps.dashboard.models import AssignAsset

def mail_expire(mail_list,asset,expire,name):
    subject = f'Regarding your {asset} expirations'
    message = f'Hi {name}, You have Not Submiitted  {asset}. The last Submisiion date is {expire} Please submit as soon as possible'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = mail_list
    send_mail( subject, message, email_from, recipient_list)




@shared_task
def send_notification_expire():
    # model = apps.get_model('apps.dashboard', 'AssignAsset')
    queryset=AssignAsset.objects.filter(expire_on__lte=datetime.now().date(),release=True)
    mail_list=[]
    for employee in queryset:
        email=employee.employee.email
        name=employee.employee.name
        asset =employee.asset
        expire=employee.expire_on
        mail_list.append(email)
        mail_expire(mail_list,asset,expire,name)
      


@shared_task
def borrow_mail(mail_list):
    subject = f'Regarding your Asset expirations'
    message = f'Hi  congratulations , You have Borrowed a Asset. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = mail_list
    send_mail( subject, message, email_from, recipient_list )

@shared_task
def asset_create_mail():
    subject = f'Regarding Asset Added'
    message = f'Hi , New Asset Added to Techbox'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mdipakpatidar@gmail.com',]
    send_mail( subject, message, email_from, recipient_list,fail_silently=False,)
    
app.conf.beat_schedule = {
"run-me-every-ten-seconds": {
"task": "tasks.send_notification_expire",
"schedule": 5.0
 }
} 
        
        




    


    