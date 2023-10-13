from django.shortcuts import get_object_or_404
from io import BytesIO
from celery import shared_task
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse


@csrf_exempt
def check_payment_status(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id')
        new_status = request.POST.get('status')
        if new_status == "InvoicePaid":
            order = get_object_or_404(Order, uuid=invoice_id)
            order.paid = True
            order.save()
            payment_completed.delay(order.id)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'My Shop – Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    out = BytesIO()
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    email.send()