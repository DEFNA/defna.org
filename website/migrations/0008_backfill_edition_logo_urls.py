from django.db import migrations

LOGO_URLS = {
    2026: "https://2026.djangocon.us/assets/img/theme/logo.svg",
    2025: "https://2025.djangocon.us/assets/img/theme/logo.svg",
    2024: "https://2024.djangocon.us/assets/img/theme/logo.svg",
    2023: "https://2023.djangocon.us/static/img/logo.svg",
    2022: "https://2022.djangocon.us/static/img/logo-2022.svg",
    2021: "https://2021.djangocon.us/static/img/logo.svg",
    2020: "https://2020.djangocon.us/static/img/logo.svg",
    2019: "https://2019.djangocon.us/static/img/logo.svg",
    2018: "https://2018.djangocon.us/static/img/logo.svg",
    2017: "https://2017.djangocon.us/static/img/logo.svg",
    2016: "https://2016.djangocon.us/site_media/static/assets/img/logo-full.59a2e37afda6.png",
    2015: "https://2015.djangocon.us/site_media/static/images/logo.png",
}


def backfill_logo_urls(apps, schema_editor):
    DjangoConEdition = apps.get_model("website", "DjangoConEdition")
    for year, logo_url in LOGO_URLS.items():
        DjangoConEdition.objects.filter(year=year, logo_url="").update(logo_url=logo_url)


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0007_seed_djangocon_editions"),
    ]

    operations = [
        migrations.RunPython(backfill_logo_urls, reverse_code=migrations.RunPython.noop),
    ]
