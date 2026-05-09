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
    # Redirects from old site URLs
    re_path(r"^events/djangoconus_\d{4}/?$", RedirectView.as_view(url="/events/djangocon/", permanent=True)),
    re_path(
        r"^announcements/\d+/\d+/\d+/(?P<slug>[\w-]+)/$",
        RedirectView.as_view(url="/blog/%(slug)s/", permanent=True),
    ),
    path(
        "defna-board-member-update-july",
        RedirectView.as_view(url="/blog/defna-board-member-update-july/", permanent=True),
    ),
    path("blm/", RedirectView.as_view(url="/", permanent=True)),
    path("events/", RedirectView.as_view(url="/events/djangocon/", permanent=True)),
    path("home-alt/", RedirectView.as_view(url="/", permanent=True)),
    path("home-alt-2/", RedirectView.as_view(url="/", permanent=True)),
    re_path(r"^category/[\w-]+/$", RedirectView.as_view(url="/blog/", permanent=True)),
]
