from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_title = "PicSizer"
admin.site.site_header = "PicSizer"
admin.site.index_title = "PicSizer"

schema_view = get_schema_view(
    openapi.Info(
        title="PicSizer API",
        default_version='v1',
        description="REST API used for image manipulation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="krzysztof.plonka64@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path("auth/", include('rest_framework.urls')),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
