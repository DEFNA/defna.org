from django.db import migrations

MILESTONES = [
    (2015, "DEFNA founded as a California nonprofit at DSF's request. First DjangoCon US held."),
    (2017, "Community grants program launched to fund Django events across North America."),
    (2021, "DjangoCon US goes fully virtual in response to COVID-19, reaching a global audience."),
    (2025, "Celebrated 20 years of Django at DjangoCon US in Chicago."),
]


def seed_milestones(apps, schema_editor):
    Milestone = apps.get_model("website", "Milestone")
    for year, description in MILESTONES:
        Milestone.objects.get_or_create(year=year, defaults={"description": description})


def unseed_milestones(apps, schema_editor):
    Milestone = apps.get_model("website", "Milestone")
    Milestone.objects.filter(year__in=[m[0] for m in MILESTONES]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0011_add_milestone"),
    ]

    operations = [
        migrations.RunPython(seed_milestones, reverse_code=unseed_milestones),
    ]
