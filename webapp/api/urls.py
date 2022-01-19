from django.urls import path, include

urlpatterns = [
    path('json/', include('api.json.urls')),
    path('path/', include('api.path.urls')),
    path('dao/', include('api.dao.urls')),
    # path('v1/', include('api.v1.urls')),
]
