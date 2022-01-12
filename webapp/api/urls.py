from django.urls import path, include

urlpatterns = [
    path('json/', include('api.json.urls')),
    # path('v1/', include('api.v1.urls')),
]
