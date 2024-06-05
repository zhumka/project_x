from django.core.mail import send_mail
from config.celery import app


@app.task
def send_test_message():

    send_mail(
        'Samirkk',
        f'Это Тестовое сообщение',
        'iptest228228@gmail.com',
        ['iptest228228@gmail.com']
    )
