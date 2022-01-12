from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings


from pathlib import Path

from shared.services import json_serv

media_root = settings.MEDIA_ROOT
json_path= Path(media_root, 'data', 'pickle.json')
serv = json_serv.Service(json_path)

@api_view(['GET'])
def get_json(resuest, key):
    obj = serv.get(key)
    return Response(obj)

