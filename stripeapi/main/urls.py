from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('buy/<int:pk>/', buy_item, name='buy_item'),
    path('item/<int:pk>/', get_item, name='get_item'),
    path('order/<str:item_ids>/', create_order, name='create_order'),
]