from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from pathlib import Path

from shared.services import tinydb_serv

## Api View Class
class TinydbListCreateDataView(views.APIView):
    """ API View to provide List and Create api for users table on tinydb """
    DB_FILE_NAME = 'tiny.json'
    #
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.JSON_DIR
    json_path = Path(media_root, target_dir, DB_FILE_NAME)
    #
    def get(self, request, table_name, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name, 'id')
        obj = serv.list()
        return Response({'data': obj})

    def post(self, request, table_name, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name, 'id')
        obj = serv.post(request.data)
        return Response({'data': obj})

## public function
list_post = TinydbListCreateDataView.as_view()

## Api View Class
class TinydbRetrieveUpdateDestroyDataView(views.APIView):
    """ API View to provide Get, Put and Delete api for users table on tinydb """
    DB_FILE_NAME = 'tiny.json'
    #
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.JSON_DIR
    json_path = Path(media_root, target_dir, DB_FILE_NAME)
    #
    def get(self, request, table_name, key, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name, 'id')
        obj = serv.get(key)
        return Response({'data': obj})

    def put(self, request, table_name, key, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name, 'id')
        obj = serv.put(request.data)
        return Response({'data': obj})

    def delete(self, request, table_name, key, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name, 'id')
        obj = serv.delete(key)
        return Response({'data': obj})

## public function
get_put_delete = TinydbRetrieveUpdateDestroyDataView.as_view()

