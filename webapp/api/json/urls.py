from django.urls import path
from . import apis_conf
from . import apis_pickle
from . import apis

urlpatterns = [
    path('<key>/', apis_pickle.root, name='get_json'),
    path('code/<key>/', apis_conf.root, name='get_codeset'),
    path('tinydb/<table_name>/', apis.list_post, name='list_and_create_table'),
    path('tinydb/<table_name>/<key>/', apis.get_put_delete, name='get_put_and_delete_record'),
]

