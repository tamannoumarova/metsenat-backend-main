"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Metsenat API system by legendary P13",
        default_version="modul-8",
        description="Metsenat  API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="umarovatamanno6@gmail.com"),
        license=openapi.License(name="PDP License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_urls = [
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("sponsors/", include("sponsors.urls")),
    path("users/", include("users.urls")),
    path("dashboard/", include("dashboard.urls")),
    # common
    path("", include("common.urls")),
]

urlpatterns += swagger_urls
