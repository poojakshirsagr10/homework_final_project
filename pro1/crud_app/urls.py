from django.urls import path
from .views import create_order, show_order, cancel_order, update_order

urlpatterns =[
    path('create/', create_order, name= 'create_url'),
    path('show/', show_order, name='show_url'),
    path('cancel/<int:pk>', cancel_order, name='cancel_url'),
    path('update/<int:pk>', update_order, name='update_url')
]