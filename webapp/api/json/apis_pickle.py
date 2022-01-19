from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from pathlib import Path

from shared.services import pickledb_serv as service

## Api View Class
class PickledbValueView(views.APIView):
    """ API View to get value with key on pickle db """
    DB_FILE_NAME = 'pickle.json'
    #
    media_root: str = settings.MEDIA_ROOT
    target_dir: str = settings.JSON_DIR
    json_path = Path(media_root, target_dir, DB_FILE_NAME)
    serv = service.Service(json_path)

    def get(self, request, key, *args, **kwargs):
        obj = self.serv.get(key)
        return Response(obj)

## public function
root = PickledbValueView.as_view()


