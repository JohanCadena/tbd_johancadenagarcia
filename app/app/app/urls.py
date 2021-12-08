from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import View
from frontend.views import IndexView, TelefoniaView
from django.contrib.auth import views as auth_views
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  #  path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', IndexView.as_view(), name='index'),
    path('telefonia/', TelefoniaView, name='telefonia'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)