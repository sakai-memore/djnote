from django.urls import path, include
from rest_framework import routers

from . import apis_address;

router = routers.SimpleRouter()
router.register('address', apis_address.AddressApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ## path('address/', apis_address.list_post, name='list_and_post_address'),
    ## path('address/<pk>/', apis_address.get_put_delete, name='get_put_and_delete_address'),
]

