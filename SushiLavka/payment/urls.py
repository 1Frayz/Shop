from django.urls import path
from . import views
from .tasks import check_payment_status

app_name = 'payment'


urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('payment/status-update/', check_payment_status, name='status_update')
]