from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from website.models import BlogPost


class BlogPostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_at

    def location(self, obj):
        return obj.get_absolute_url()


class StaticPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return [
            "home",
            "about",
            "djangocon",
            "sponsored-events",
            "donate",
            "grants",
            "contact",
            "venue-host",
            "blog",
        ]

    def location(self, item):
        return reverse(item)


SITEMAPS = {
    "static": StaticPageSitemap,
    "blog": BlogPostSitemap,
}
