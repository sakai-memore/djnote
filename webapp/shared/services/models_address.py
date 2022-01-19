from django.db import models
from django.utils import timezone
from rest_framework import serializers
from django.contrib import admin

class AddressModel(modles.Model):
    """ Address Model """
    class Meta:
        db_table = 'Address'

    ## definition fields
    address_id = models.AutoField(null=True)
    address = models.CharField(max_length='50', null=True)
    address2 = models.CharField(max_length='50')
    district = models.CharField(max_length='20', null=True)
    city_id = models.IntegerField(null=True)
    postal_code = models.CharField(max_length='10')
    phone = models.CharField(max_length='20', null=True)
    last_update = models.DateTimeField(max_length='6', null=True)

    ## def __str__
    def __str__(self):
        return self.address_id

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'

class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('address_id','address','address2','district','city_id','postal_code','phone','last_update')
    ordering = ('address_id',)

admin.site.register(AddressModel, AddressModelAdmin)

