from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from website.models import Announcement
from website.models import BlogPost
from website.models import BoardMember
from website.models import DjangoConEdition
from website.models import GrantCycle
from website.models import Milestone
from website.models import SponsoredEvent


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["announcements"] = Announcement.objects.all()[:4]
        ctx["featured"] = Announcement.objects.filter(is_featured=True).first()
        return ctx


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["board"] = BoardMember.objects.filter(is_current=True)
        ctx["emeritus"] = BoardMember.objects.filter(is_current=False, is_emeritus=True)
        ctx["alumni"] = BoardMember.objects.filter(is_current=False, is_emeritus=False)
        ctx["milestones"] = Milestone.objects.all()
        return ctx


class DjangoConView(ListView):
    template_name = "events/djangocon.html"
    context_object_name = "editions"
    queryset = DjangoConEdition.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["upcoming"] = DjangoConEdition.objects.filter(status=DjangoConEdition.Status.UPCOMING).first()
        return ctx


class SponsoredEventsView(ListView):
    template_name = "events/sponsored.html"
    context_object_name = "events"
    queryset = SponsoredEvent.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grant_cycle"] = GrantCycle.objects.order_by("-id").first()
        return ctx


class DonateView(TemplateView):
    template_name = "donate.html"


GRANT_ELIGIBILITY = [
    "The event must be Django-related (meetup, workshop, conference, or sprint).",
    "Events of all sizes are welcome — from small local meetups to regional conferences.",
    "Grant funds must be used for event costs.",
]


class GrantsView(TemplateView):
    template_name = "grants.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cycle"] = GrantCycle.objects.order_by("-id").first()
        ctx["eligibility_items"] = GRANT_ELIGIBILITY
        return ctx


class ContactView(TemplateView):
    template_name = "contact.html"


class BlogListView(ListView):
    template_name = "blog/list.html"
    context_object_name = "posts"
    paginate_by = 9
    queryset = BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    context_object_name = "post"
    queryset = BlogPost.objects.filter(is_published=True)


class VenueHostView(TemplateView):
    template_name = "events/venue-host.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["venue_basic"] = [
            "Name",
            "Location",
            "Transportation options (how do people get there from the airport?)",
            "Attendance capacity",
        ]
        ctx["venue_spaces"] = [
            "Keynote room (also Sessions Track A) to accommodate up to 450 people, classroom style (tables with chairs)",
            "Room for Sessions Track B to accommodate up to 200 people, classroom style (tables with chairs)",
            "Space for sponsors to set up exhibit booths/tables — at least 12, and up to 16, sponsors with either 6' tables or 10'×10' booth spaces",
            "Green room for speakers to prepare (generally a room that will seat 25 for a workshop is the right size)",
            "Space for registration tables",
            "Room for meals and breaks with sufficient seating and tables — if capacity is under 450, indicate room capacity and time required to move 450 people through",
            "Space for supplemental beverage stations for daylong service",
            "Secure overnight storage for vendor booth supplies and conference registration desk items",
        ]
        ctx["venue_catering"] = [
            "450 people per day during the main conference: breakfast, morning break, lunch, afternoon break, and all-day beverage service",
            "Options for celiacs, vegetarians, and vegans of equal quality and variety as the main menu — estimate 15% vegetarian, 5% vegan, and 5–10% gluten-free",
            "Ability to serve a meal to 350–450 people within a 90-minute window",
            "Most venues require use of their in-house catering. If not, note whether outside catering vendors are restricted to an approved list and any requirements they must meet",
        ]
        ctx["venue_qualities"] = [
            "Easy to reach from the airport and the conference hotel",
            "Adjoins or within walking distance of a suitable hotel which can accommodate 350–450 attendees",
            "Excellent internet connectivity",
            "Accessible to as many attendees as possible",
            "Reasonable access to transit for sightseeing",
            "Gender-neutral (or at least gender-inclusive) restrooms within a short walk of the conference rooms",
        ]
        ctx["sprint_basic"] = [
            "Name",
            "Location",
            "Transportation options (how do people get there from the hotel?)",
            "Attendance capacity",
        ]
        ctx["sprint_qualities"] = [
            "Easy to reach from the conference hotel",
            "A room to hold 50–75 people with work tables, chairs, power, and internet connectivity",
            "Eating tables should be separate from work tables if at all possible",
            "Excellent internet connectivity",
        ]
        ctx["hotel_details"] = [
            "Name",
            "Location",
            "Transportation options (how do people get there from the airport?)",
            "The conference room rate (should be discounted from the standard rate)",
            "A room block covering the two nights before tutorials through the last night of the sprints",
            "Concessions policy (comp room nights per actualised room nights)",
            "A sample contract showing the terms of booking the block of rooms — do not sign anything",
        ]
        ctx["hotel_room_block"] = [
            {"night": "Friday (2 nights before tutorials)", "rooms": 10},
            {"night": "Saturday (1 night before tutorials)", "rooms": 15},
            {"night": "Sunday — Tutorials", "rooms": 100},
            {"night": "Monday — Main Conference", "rooms": 100},
            {"night": "Tuesday — Main Conference", "rooms": 100},
            {"night": "Wednesday — Main Conference", "rooms": 80},
            {"night": "Thursday — Sprints", "rooms": 30},
            {"night": "Friday — Sprints", "rooms": 15},
        ]
        ctx["hub_cities"] = [
            "New York",
            "Los Angeles",
            "San Francisco",
            "Atlanta",
            "Dallas",
            "Chicago",
            "London",
        ]
        return ctx
