from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from django.views.static import serve

from config import __version__
from health_check.views import HealthCheckView
from website.sitemaps import SITEMAPS

admin_header = f"DEFNA v{__version__}"
admin.site.enable_nav_sidebar = False
admin.site.site_header = admin_header
admin.site.site_title = admin_header

urlpatterns = [
    path("", include("website.urls")),
    path("accounts/", include("allauth.urls")),
    path("markdownx/", include("markdownx.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "health/",
        HealthCheckView.as_view(
            checks=[
                # "health_check.Cache",
                "health_check.Database",
                "health_check.Storage",
            ]
        ),
    ),
    path("sitemap.xml", sitemap, {"sitemaps": SITEMAPS}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
