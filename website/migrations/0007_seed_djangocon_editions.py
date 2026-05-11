import datetime

from django.db import migrations

EDITIONS = [
    {
        "year": 2026,
        "start_date": datetime.date(2026, 8, 24),
        "end_date": datetime.date(2026, 8, 28),
        "location": "Chicago, Illinois",
        "website_url": "https://2026.djangocon.us",
        "logo_url": "https://2026.djangocon.us/assets/img/theme/logo.svg",
        "status": "upcoming",
        "highlight": "voco Chicago Downtown — talks, tutorials, and sprints with opportunity grants available.",
    },
    {
        "year": 2025,
        "start_date": datetime.date(2025, 9, 8),
        "end_date": datetime.date(2025, 9, 12),
        "location": "Chicago, Illinois",
        "website_url": "https://2025.djangocon.us",
        "logo_url": "https://2025.djangocon.us/assets/img/theme/logo.svg",
        "status": "completed",
        "highlight": "voco Chicago Downtown — celebrating 20 years of Django with talks, tutorials, and sprints.",
    },
    {
        "year": 2024,
        "start_date": datetime.date(2024, 9, 22),
        "end_date": datetime.date(2024, 9, 27),
        "location": "Durham, North Carolina",
        "website_url": "https://2024.djangocon.us",
        "logo_url": "https://2024.djangocon.us/assets/img/theme/logo.svg",
        "status": "completed",
        "highlight": "Over 300 attendees and 50+ talks and tutorials.",
    },
    {
        "year": 2023,
        "start_date": datetime.date(2023, 10, 16),
        "end_date": datetime.date(2023, 10, 20),
        "location": "Durham, North Carolina",
        "website_url": "https://2023.djangocon.us",
        "logo_url": "https://2023.djangocon.us/static/img/logo.svg",
        "status": "completed",
        "highlight": "Durham Convention Center.",
    },
    {
        "year": 2022,
        "start_date": datetime.date(2022, 10, 16),
        "end_date": datetime.date(2022, 10, 21),
        "location": "San Diego, California",
        "website_url": "https://2022.djangocon.us",
        "logo_url": "https://2022.djangocon.us/static/img/logo-2022.svg",
        "status": "completed",
        "highlight": "San Diego Marriott Mission Valley.",
    },
    {
        "year": 2021,
        "start_date": datetime.date(2021, 10, 22),
        "end_date": datetime.date(2021, 10, 23),
        "location": "Online",
        "website_url": "https://2021.djangocon.us",
        "logo_url": "https://2021.djangocon.us/static/img/logo.svg",
        "status": "virtual",
        "highlight": "Fully virtual edition — no tutorials or sprints.",
    },
    {
        "year": 2020,
        "start_date": datetime.date(2020, 10, 11),
        "end_date": datetime.date(2020, 10, 16),
        "location": "San Diego, California",
        "website_url": "https://2020.djangocon.us",
        "logo_url": "https://2020.djangocon.us/static/img/logo.svg",
        "status": "cancelled",
        "highlight": "Cancelled due to COVID-19.",
    },
    {
        "year": 2019,
        "start_date": datetime.date(2019, 9, 22),
        "end_date": datetime.date(2019, 9, 27),
        "location": "San Diego, California",
        "website_url": "https://2019.djangocon.us",
        "logo_url": "https://2019.djangocon.us/static/img/logo.svg",
        "status": "completed",
        "highlight": "San Diego Marriott Mission Valley.",
    },
    {
        "year": 2018,
        "start_date": datetime.date(2018, 10, 14),
        "end_date": datetime.date(2018, 10, 19),
        "location": "San Diego, California",
        "website_url": "https://2018.djangocon.us",
        "logo_url": "https://2018.djangocon.us/static/img/logo.svg",
        "status": "completed",
        "highlight": "San Diego Marriott Mission Valley.",
    },
    {
        "year": 2017,
        "start_date": datetime.date(2017, 8, 13),
        "end_date": datetime.date(2017, 8, 18),
        "location": "Spokane, Washington",
        "website_url": "https://2017.djangocon.us",
        "logo_url": "/static/images/spokane.png",
        "status": "completed",
        "highlight": "Hotel RL by Red Lion.",
    },
    {
        "year": 2016,
        "start_date": datetime.date(2016, 7, 17),
        "end_date": datetime.date(2016, 7, 22),
        "location": "Philadelphia, Pennsylvania",
        "website_url": "https://2016.djangocon.us",
        "logo_url": "https://2016.djangocon.us/site_media/static/assets/img/logo-full.59a2e37afda6.png",
        "status": "completed",
        "highlight": "The Wharton School, University of Pennsylvania.",
    },
    {
        "year": 2015,
        "start_date": datetime.date(2015, 9, 6),
        "end_date": datetime.date(2015, 9, 11),
        "location": "Austin, Texas",
        "website_url": "https://2015.djangocon.us",
        "logo_url": "https://2015.djangocon.us/site_media/static/images/logo.png",
        "status": "completed",
        "highlight": "",
    },
]


def seed_editions(apps, schema_editor):
    DjangoConEdition = apps.get_model("website", "DjangoConEdition")
    for data in EDITIONS:
        year = data.pop("year")
        DjangoConEdition.objects.update_or_create(year=year, defaults=data)
        data["year"] = year


def unseed_editions(apps, schema_editor):
    DjangoConEdition = apps.get_model("website", "DjangoConEdition")
    DjangoConEdition.objects.filter(year__in=[e["year"] for e in EDITIONS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0006_djangoconedition_logo_url"),
    ]

    operations = [
        migrations.RunPython(seed_editions, reverse_code=unseed_editions),
    ]
