from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.root, name='modeler'),
    path('new/', views.root, name='modeler_new'),
]
