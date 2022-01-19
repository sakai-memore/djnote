from rest_framework import viewsets
from django_filters import rest_framework as filters

from shared.dataobjects import address as dao

class AddressFilter(filters.FilterSet):
    """ Address filter class """
    
    class Meta:
        model = dao.AddressModel
        fields = ['address_id','address','address2','district','city_id','postal_code','phone','last_update']

class AddressApiViewSet(viewsets.ModelViewSet):
    """ Address api view """
    queryset = dao.AddressModel.objects.all()
    serializer_class = dao.AddressSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AddressFilter

list_post = AddressApiViewSet.as_view({'get': 'list', 'post': 'create'})
get_put_delete = AddressApiViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
