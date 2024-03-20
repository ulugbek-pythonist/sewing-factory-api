from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import MaterialRequirementsView, ProductViewSet


router = DefaultRouter()
router.register("products", ProductViewSet)


urlpatterns = [
    path(
        "material-requirements/",
        MaterialRequirementsView.as_view(),
        name="material-requirements",
    ),
    path("", include(router.urls)),
]
