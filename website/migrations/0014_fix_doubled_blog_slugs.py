from django.db import migrations

# Mapping of broken (doubled/truncated) slugs to correct filename-based slugs.
# The import script filled the slug field via Django admin, but admin JS had
# already auto-populated a title-derived slug, producing doubled values
# truncated at 50 chars.
SLUG_FIXES = {
    "djangocon-us-2016-in-phillydjangocon-us-2016-in-ph": "2016-02-10-djangocon-us-2016-in-philly",
    "djangocon-us-call-for-venue-proposal-2017djangocon": "2016-06-08-djangocon-us-call-for-venue-proposal-2017",
    "defna-phase-iidefna-phase-ii": "2016-07-20-defna-phase-ii",
    "djangocon-us-2017-in-spokane-washingtondjangocon-u": "2016-12-01-djangocon-us-2017-in-spokane-washington",
    "defna-board-member-recruitment-join-usdefna-board-": "2017-04-04-defna-board-member-recruitment-join-us",
    "djangocon-us-call-for-venue-proposal-2018-and-2019": "2017-05-10-djangocon-us-call-for-venue-proposal-2018-and-2019",
    "two-weeks-left-to-submit-djangocon-venue-proposals": "2017-07-19-two-weeks-left-to-submit-djangocon-venue-proposals-for-2018-and-2019",
    "welcome-new-board-memberswelcome-new-board-members": "2017-07-20-welcome-new-board-members",
    "the-joys-of-catering-part-1-tickets-sold-does-nott": "2017-08-01-the-joys-of-catering-part-1",
    "call-for-proposals-for-djangocon-2018-websitecall-": "2017-10-12-call-for-proposals-for-djangocon-2018-website",
    "djangocon-us-2018-in-san-diegodjangocon-us-2018-in": "2017-11-02-djangocon-us-2018-in-san-diego",
    "join-defna-board-member-recruitmentjoin-defna-boar": "2018-01-23-join-defna-board-member-recruitment",
    "semester-grants-reportsemester-grants-report": "2018-09-10-semester-grants-report",
    "congratulations-jeffcongratulations-jeff": "2018-09-24-congratulations-jeff",
    "board-updatesboard-updates": "2020-03-02-board-updates",
    "vendor-updatevendor-update": "2020-04-15-vendor-update",
    "djangocon-us-2020-videodjangocon-us-2020-video": "2020-10-21-djangocon-us-2020-video",
    "djangocon-us-2020djangocon-us-2020": "2020-10-30-djangocon-us-2020",
    "join-defna-board-member-recruitmentdefna-board-mem": "2022-02-02-defna-board-member-recruitment",
    "djangocon-us-2022-is-livedjangoconus-2022-live": "2022-05-10-djangoconus-2022-live",
    "djangocon-us-call-for-venue-proposal-2023djangocon": "2022-05-20-djangocon-us-call-for-venue-proposal-2023",
    "call-for-proposals-for-djangocon-us-2023-websiteca": "2023-01-01-call-for-proposals-for-djangocon-2023-website",
    "board-member-update-for-2023board-updates": "2023-02-02-board-updates",
    "board-member-update-for-july-2023board-updates": "2023-07-24-board-updates",
    "call-for-proposals-for-djangocon-us-2024-websiteca": "2024-01-12-call-for-proposals-for-djangocon-us-2024-website",
    "djangocon-us-2024-has-been-announceddjangoconus-20": "2024-01-17-djangoconus-2024-announced",
    "board-member-update-for-may-2024board-updates": "2024-05-01-board-updates",
    "djangocon-us-call-for-venue-proposal-2025djangocon": "2024-05-28-djangocon-us-call-for-venue-proposal-2025",
    "djangocon-us-call-for-venue-proposal-2025-extensio": "2024-10-16-djangocon-us-call-for-venue-proposal-2025-extension",
    "djangocon-us-2025-has-been-announceddjangoconus-20": "2024-12-31-djangoconus-2025-announced",
    "board-member-update-for-20252025-07-18-defna-board": "2025-07-18-defna-board-member-update-july",
    "djangocon-us-call-for-venue-proposals-2027-28call-": "2025-09-10-call-for-venue-proposal-2027",
    "call-for-proposals-for-djangocon-us-2026-websiteca": "2026-01-12-call-for-proposals-for-djangocon-us-2026-website",
    "celebrating-20-years-of-django-looking-back-moving": "2025-07-21-celebrating-20-years-of-django",
}


def fix_slugs(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    for old_slug, new_slug in SLUG_FIXES.items():
        BlogPost.objects.filter(slug=old_slug).update(slug=new_slug)


def unfix_slugs(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    for old_slug, new_slug in SLUG_FIXES.items():
        BlogPost.objects.filter(slug=new_slug).update(slug=old_slug)


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0013_fix_blogpost_slug_max_length"),
    ]

    operations = [
        migrations.RunPython(fix_slugs, unfix_slugs),
    ]
