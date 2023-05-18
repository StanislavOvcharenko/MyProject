from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

@shared_task
def send_activate_mail(username, email):
    subject = 'Активація аккаунта'
    message = f'''
            Активація акакаунту: {settings.HTTP_SCHEMA}://{settings.DOMAIN}{reverse('accounts:activate',
                                                                                args=(username,))}'''

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


@shared_task
def send_link_for_comment(check_number, email):
    subject = 'Відгук про станцію'
    message = f'''
               Залиште відгук тут: {settings.HTTP_SCHEMA}://{settings.DOMAIN}{
    reverse('comments_and_rating:create_comments_and_rating',args=(check_number,))}'''

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )