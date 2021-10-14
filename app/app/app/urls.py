from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import View
from frontend.views import IndexView
from django.contrib.auth import views as auth_views
from django.conf import Settings, settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)