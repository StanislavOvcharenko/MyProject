from django.contrib import admin
from django.urls import path, include
from autohistory.views import IndexView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('autohistory/', include('autohistory.urls')),
    path('comments_and_rating/', include('comments_and_rating.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
