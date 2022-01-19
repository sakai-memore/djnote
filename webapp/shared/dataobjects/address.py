from django.db import models
from django.utils import timezone
from rest_framework import serializers
from django.contrib import admin

class AddressModel(models.Model):
    """ Address Model """
    class Meta:
        db_table = 'Address'

    ## definition fields
    address_id = models.BigAutoField(primary_key=True, null=False)
    address = models.CharField(max_length=50, null=False)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=20, null=False)
    city_id = models.IntegerField(null=False)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=False)
    last_update = models.DateTimeField(null=True, blank=True)

    ## def __str__
    def __str__(self):
        return self.address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'

class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('address_id','address','address2','district','city_id','postal_code','phone','last_update')
    ordering = ('address_id',)

admin.site.register(AddressModel, AddressModelAdmin)
