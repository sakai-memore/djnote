from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from shared.services import conf_serv as service


## Api View Class
class CodesetView(views.APIView):
    """ API View to get code set from config.services """
    #
    serv = service.Service()
    #
    def get(self, request, key, *args, **kwargs):
        obj = self.serv.get(key)
        return Response(obj)

## public function
root =CodesetView.as_view()


