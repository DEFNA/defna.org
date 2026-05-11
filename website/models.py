from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from django.urls import reverse


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class BoardMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="board/", blank=True)
    twitter_url = models.URLField(blank=True, verbose_name="X (Twitter) URL")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    mastodon_url = models.URLField(blank=True, verbose_name="Mastodon URL")
    bluesky_url = models.URLField(blank=True, verbose_name="Bluesky URL")
    website_url = models.URLField(blank=True, verbose_name="Website URL")
    is_current = models.BooleanField(default=True)
    is_emeritus = models.BooleanField(default=False, help_text="Honour past members who went above and beyond.")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.role})"


class DjangoConEdition(models.Model):
    class Status(models.TextChoices):
        UPCOMING = "upcoming", "Upcoming"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"
        VIRTUAL = "virtual", "Virtual"

    year = models.PositiveSmallIntegerField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    website_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True, verbose_name="Logo URL")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPCOMING)
    highlight = models.TextField(blank=True, help_text="One-line summary shown in the edition card and timeline.")

    class Meta:
        ordering = ["-year"]
        verbose_name = "DjangoCon Edition"
        verbose_name_plural = "DjangoCon Editions"

    def __str__(self):
        return f"DjangoCon US {self.year}"


class SponsoredEvent(models.Model):
    name = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200)
    event_date = models.DateField()
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True)
    grant_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return f"{self.name} ({self.location})"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(help_text="Short summary shown in the post listing.")
    body = MarkdownxField()
    author = models.CharField(max_length=100, blank=True)
    cover_image = models.ImageField(upload_to="blog/", blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Blog Post"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})


class Milestone(models.Model):
    year = models.PositiveSmallIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ["year"]

    def __str__(self):
        return f"{self.year}: {self.description[:60]}"


class GrantCycle(models.Model):
    is_open = models.BooleanField(default=False)
    application_url = models.URLField(blank=True)
    max_amount = models.DecimalField(max_digits=8, decimal_places=2, default=300)
    deadline = models.DateField(null=True, blank=True)
    description = models.TextField(help_text="Guidance text shown on the grants page.")

    class Meta:
        verbose_name = "Grant Cycle"

    def __str__(self):
        status = "Open" if self.is_open else "Closed"
        return f"Grant Cycle ({status})"
