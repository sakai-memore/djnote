from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.create, name="create"),
    # path(r'^password-change-done/$', views.password_change_done, name='password_change_done'),
]
