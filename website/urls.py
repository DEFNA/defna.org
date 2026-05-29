from django.urls import path, re_path
from django.views.generic import RedirectView

from website import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("events/djangocon/", views.DjangoConView.as_view(), name="djangocon"),
    path("events/sponsored/", views.SponsoredEventsView.as_view(), name="sponsored-events"),
    path("donate/", views.DonateView.as_view(), name="donate"),
    path("grants/", views.GrantsView.as_view(), name="grants"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("events/venue-host/", views.VenueHostView.as_view(), name="venue-host"),
    path("blog/", views.BlogListView.as_view(), name="blog"),
    path("blog/<slug:slug>/", views.BlogDetailView.as_view(), name="blog-detail"),
    # Pattern-based redirects from old site
    re_path(r"^events/djangoconus_\d{4}/?$", RedirectView.as_view(url="/events/djangocon/", permanent=True)),
    path("events/", RedirectView.as_view(url="/events/djangocon/", permanent=True)),
    re_path(r"^category/[\w-]+/$", RedirectView.as_view(url="/blog/", permanent=True)),
]
