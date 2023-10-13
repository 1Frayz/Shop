from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from .forms import OrderCreateForm, PaymentForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse
from shop.recommender import Recommender


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        payment_methods = PaymentForm(request.POST) 
        if form.is_valid() and payment_methods.is_valid():  
            payment_method = payment_methods.cleaned_data['payment_method']
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            r = Recommender()
            recommender = []
            for item in cart:
                recommender.append(item['product'])
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            r.products_bought(recommender)
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id'] = order.id
            if payment_method == 'cash':
                return redirect(reverse('orders:order_created'))
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
        payment_methods = PaymentForm() 

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, 'payment_methods': payment_methods})


def created(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order/created.html', {'order': order})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})