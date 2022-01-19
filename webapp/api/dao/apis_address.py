from rest_framework import viewsets
from django_filters import rest_framework as filters

from shared.dataobjects import address as dao

class AddressFilter(filters.FilterSet):
    """ Address filter class """
    # 
    class Meta:
        model = dao.AddressModel

class AddressApiViewSet(viewsets.ModelViewSet):
    """ Address api view """
    queryset = dao.AddressModel.objects.all()
    serializer_class = dao.AddressSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AddressFilter

root = AddressApiViewSet.as_view()
