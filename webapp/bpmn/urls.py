from django.urls import path, include

urlpatterns = [
    path('viewer/', include('bpmn.viewer.urls')),
    path('modeler/', include('bpmn.modeler.urls')),
]
