from django.urls import path, re_path
from . import apis_conf
from . import apis_pickle
from . import apis
from . import apis_datatable

urlpatterns = [
    path('code/<key>/', apis_conf.root, name='get_codeset'),
    path('tinydb/<table_name>/', apis.list_post, name='list_and_create_table'),
    path('tinydb/<table_name>/<str:key>/', apis.get_put_delete, name='get_put_and_delete_record'),
    path('t/<table_name>/', apis_datatable.list_post, name='list_and_create_table_api'),
    path('t/<table_name>/<str:key>/', apis_datatable.get_put_delete, name='get_put_and_delete_record_api'),
    path('p/<table_name>/<str:key>/', apis_pickle.root, name='get_json'),
]

