from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from orders.models import Order
import base64
import hashlib
import json
import requests
import uuid


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)

    for item in order.items.all():
        request = {
            'externalId': str(uuid.uuid4()),
            'amount': int(item.price)*int(item.quantity),
            'currency': 'RUB',
            'description': 'Create invoice',
            'deliveryMethod': 'URL',
            'successUrl': 'http://127.0.0.1:8000/2/legkost/',
        }

    req_str = json.dumps(request)
    str_ = req_str + settings.SECRET_PHRASE
    md5 = hashlib.md5(str_.encode())
    sign = base64.b64encode(md5.digest()).decode('utf-8')

    _headers = {
        'X-Api-key': settings.API_KEY,
        'X-sign': sign,
        'Content-type': 'application/json'
    }

    session = requests.post(url=settings.URL, json=request, headers=_headers)
    status_code = session.status_code
    body = session.content.decode('utf-8')
    resp_body = json.loads(body)
    order.uuid = resp_body["data"]["uuid"]
    order.save()
    return redirect(resp_body["data"]["paymentLink"], code=303)

