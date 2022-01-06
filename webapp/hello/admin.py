from django.contrib import admin

from hello.entities import models 


class BookModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')

class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


admin.site.register(models.Book, BookModelAdmin)
admin.site.register(models.Author, AuthorModelAdmin)
admin.site.register(models.Publisher, PublisherModelAdmin)
