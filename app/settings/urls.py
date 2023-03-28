
from django.contrib import admin
from django.urls import path
from autohistory.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world)
]
