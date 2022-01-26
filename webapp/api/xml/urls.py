from django.urls import path
from . import apis

urlpatterns = [
    path('get/<file_name>/', apis.get_filename, name='get_xmlname'),
    path('exist/<file_name>/', apis.exist, name='exist_xmlname'),
]

