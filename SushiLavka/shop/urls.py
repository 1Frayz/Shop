from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('detail/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
