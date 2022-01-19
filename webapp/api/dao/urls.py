from django.urls import path

from . import apis_address; 

urlpatterns = [
    path('address/', apis_address.list_post, name='list_and_post_address'),
    path('address/<pk>/', apis_address.get_put_delete, name='get_put_and_delete_address'),
]

