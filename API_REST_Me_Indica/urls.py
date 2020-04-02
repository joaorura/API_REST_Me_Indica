from django.contrib import admin
from django.urls import path, include
from .api.urls import urlpatterns as url
urlpatterns = [
    path(r'admin/', admin.site.urls),
]

urlpatterns += url
