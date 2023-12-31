from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore
from rest_framework.permissions import IsAdminUser

schema_view = get_schema_view(
    openapi.Info(
        title="Service API",
        default_version="v1",
        description="Service API docs",
    ),
    public=True,
    permission_classes=[IsAdminUser],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
