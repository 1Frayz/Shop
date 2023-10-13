from django.urls import path
from . import views

app_name = 'info'


urlpatterns = [
    path('map/', views.map, name='map'),
    path('info/', views.info, name='info'),
]
