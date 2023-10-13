from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}'
    message = f'Уважаемый(ая) {order.first_name},\n\nВы успешно оформили заказ. Номер вашего заказа: {order.id}.'
    mail_sent = send_mail(subject,message, 'admin@myshop.com', [order.email])
    return mail_sent