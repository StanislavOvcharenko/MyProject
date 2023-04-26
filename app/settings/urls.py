from django.contrib import admin
from django.urls import path, include
from autohistory.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('autohistory/', include('autohistory.urls')),
    path('comments_and_rating/', include('comments_and_rating.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]
