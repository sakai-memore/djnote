from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from pathlib import Path

from shared.services import pickledb_serv as service

## Api View Class
class PickledbValueView(views.APIView):
    """ API View to get value with key on pickle db """
    #
    media_dir : str = settings.MEDIA_DIR
    target_dir: str = settings.JSON_DIR
    JSON_FILE_NAME : str = 'pickle.json'
    json_path = Path(media_dir, target_dir, JSON_FILE_NAME)
    serv = service.Service(json_path)

    def get(self, request, table_name, key, *args, **kwargs):
        obj = self.serv.get(table_name)
        # 
        lst = []
        if key == 'all':
            extracted = obj
            for k in extracted:
                lst.append(extracted[k])
        elif key in obj:
            lst.append(obj[key])
        else:
            lst.append({})
        #
        return Response({'data': lst})


## public function
root = PickledbValueView.as_view()

