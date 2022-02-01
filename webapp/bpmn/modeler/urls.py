from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.root, name='modeler'),
    path('copy/<str:pk>', views.root, name='modeler_copy'),
    path('new/', views.new, name='modeler_new'),
]
