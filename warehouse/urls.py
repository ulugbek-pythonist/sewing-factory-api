from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import GetRemaindersAPIView, HealtCheckView


urlpatterns = [
    path("health-check/",HealtCheckView.as_view(),name="health-check"),
    path("warehouse/",GetRemaindersAPIView.as_view(),name="warehouse"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)