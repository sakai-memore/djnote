from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from shared.services import xml_path_serv

## Api View Class
class XmlPathView(views.APIView):
    """ API View to get xml path with key """

    media_root = settings.MEDIA_ROOT
    serv = xml_path_serv.Service(media_root)

    def get(self, request, key, *args, **kwargs):
        xml = self.serv.get(key)
        return Response(xml)

## public function
get_xml = XmlPathView.as_view()

