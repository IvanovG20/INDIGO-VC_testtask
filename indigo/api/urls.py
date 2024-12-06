from django.urls import path, include, re_path

from rest_framework.routers import SimpleRouter

from api.views import FilmViewSet, favorites


app_name = 'api'


router_v1 = SimpleRouter()
router_v1.register('films', FilmViewSet, basename='films')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    re_path(r'users/(?:(me)|(\d+))/favorites/$', favorites),
    path('auth/', include('djoser.urls.authtoken')),
]
