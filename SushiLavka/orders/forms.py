from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField

PAYMENT_CHOICES = [
    ('cash', 'Наличными'),
    ('card', 'Картой'),
]

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        label='Выберите способ оплаты',
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect,  
    )


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'phone', 'delivery', 'address', 'comment', 'delivery_date']

    first_name = forms.CharField(max_length=50, label="Имя")
    phone = PhoneNumberField(label="Номер телефона")
    delivery = forms.BooleanField(required=False, label="Доставка")
    address = forms.CharField(max_length=250, required=False, label="Адреc")
    comment = forms.CharField(max_length=250, required=False, label="Комментарий")
    delivery_date = forms.DateTimeField(required=True, label="Дата доставки")
