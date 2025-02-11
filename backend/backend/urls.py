from django.contrib import admin
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docks"),
    path("/", include("song.urls")),
]
