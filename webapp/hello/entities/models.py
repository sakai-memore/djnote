import uuid

from django.db import models
from django.utils import timezone
from rest_framework import serializers

class Publisher(models.Model):
    """ Publisher Model"""
    class Meta:
        db_table = 'publisher'

    ## definition columns
    name = models.CharField(max_length=255)

    ## def __str__
    def __str__(self):
        return self.name

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class Author(models.Model):
    """ Author Model"""
    class Meta:
        db_table = 'author'

    ## definition columns
    name = models.CharField(max_length=255)

    ## def __str__
    def __str__(self):
        return self.name

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class Book(models.Model):
    """ Book Model"""
    class Meta:
        db_table = 'book'

    ## definition columns
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    publish_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    ## def __str__
    def __str__(self):
        return f'{{"id": "{self.id}", "title": "{self.title}"}}'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

