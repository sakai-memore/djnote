from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from pathlib import Path

from shared.services import path_serv as service


## Api View Class
class FileNameView(views.APIView):
    """ API View to exist or not """
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.XML_DIR
    #
    def get(self, request, file_name, *args, **kwargs):
        serv = service.Service(self.media_root, self.target_dir)
        obj = serv.get_filename(file_name)
        return Response(obj)

## public function
get_filename = FileNameView.as_view()


## Api View Class
class ExistFileView(views.APIView):
    """ API View to get file name """
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.XML_DIR
    target_path: Path
    #
    def get(self, request, file_name, *args, **kwargs):
        serv = service.Service(self.media_root, self.target_dir)
        exist = serv.exist(file_name)
        return Response({'result': exist})

## public function
exist = ExistFileView.as_view()

