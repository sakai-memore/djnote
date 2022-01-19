from django.urls import path
from . import apis

urlpatterns = [
    path('<key>/', apis.get_xml, name='get_xml'),
]

