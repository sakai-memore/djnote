from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from pathlib import Path

from shared.services import tinydb_serv

## Api View Class
class TinydbListCreateView(views.APIView):
    """ API View to provide List and Create api for users table on tinydb """
    DB_FILE_NAME = 'tiny.json'
    #
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.JSON_DIR
    json_path = Path(media_root, target_dir, DB_FILE_NAME)
    #
    def get(self, request, table_name, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name)
        obj = serv.list()
        return Response(obj)

    def post(self, request, table_name, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name)
        obj = serv.post(request.data)
        return Response(obj)

## public function
list_post = TinydbListCreateView.as_view()

## Api View Class
class TinydbRetrieveUpdateDestroyView(views.APIView):
    """ API View to provide Get, Put and Delete api for users table on tinydb """
    DB_FILE_NAME = 'tiny.json'
    #
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.JSON_DIR
    json_path = Path(media_root, target_dir, DB_FILE_NAME)
    #
    def get(self, request, table_name, key, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name)
        obj = serv.get(key)
        return Response(obj)

    def put(self, request, table_name, key, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name)
        obj = serv.put(request.data)
        return Response(obj)

    def delete(self, request, table_name, key, *args, **kwargs):
        serv = tinydb_serv.Service(self.json_path, table_name)
        obj = serv.delete(key)
        return Response(obj)

## public function
get_put_delete = TinydbRetrieveUpdateDestroyView.as_view()

