from django.db import migrations


def fix_2017_logo(apps, schema_editor):
    DjangoConEdition = apps.get_model("website", "DjangoConEdition")
    DjangoConEdition.objects.filter(year=2017).update(logo_url="/static/images/spokane.png")


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0009_fix_edition_logo_urls"),
    ]

    operations = [
        migrations.RunPython(fix_2017_logo, reverse_code=migrations.RunPython.noop),
    ]
