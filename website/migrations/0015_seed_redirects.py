from django.db import migrations

# Old URL path → new URL path
# Sourced from issue #11 and old.defna.org sitemap
REDIRECTS = [
    # Blog post redirects (old announcements → new blog URLs)
    ("/announcements/2016/2/9/djangocon-us-2016-in-philly/", "/blog/2016-02-10-djangocon-us-2016-in-philly/"),
    ("/announcements/2016/6/8/djangocon-us-call-for-venue-proposal-2017/", "/blog/2016-06-08-djangocon-us-call-for-venue-proposal-2017/"),
    ("/announcements/2016/7/20/defna-phase-ii/", "/blog/2016-07-20-defna-phase-ii/"),
    ("/announcements/2016/11/30/djangocon-us-2017-in-spokane/", "/blog/2016-12-01-djangocon-us-2017-in-spokane-washington/"),
    ("/announcements/2017/04/03/join-us/", "/blog/2017-04-04-defna-board-member-recruitment-join-us/"),
    ("/announcements/2017/5/10/djangocon-us-call-for-venue-proposal-2018-and-2019/", "/blog/2017-05-10-djangocon-us-call-for-venue-proposal-2018-and-2019/"),
    ("/announcements/2017/7/19/welcome-new-board-members/", "/blog/2017-07-20-welcome-new-board-members/"),
    ("/announcements/2017/7/25/the-joys-of-catering-part-1-tickets-sold-does-not-equal-catering-count/", "/blog/2017-08-01-the-joys-of-catering-part-1/"),
    ("/announcements/2017/10/10/call-for-proposals-for-djangocon-2018-website/", "/blog/2017-10-12-call-for-proposals-for-djangocon-2018-website/"),
    ("/announcements/2017/11/2/djangocon-us-2018-in-san-diego/", "/blog/2017-11-02-djangocon-us-2018-in-san-diego/"),
    ("/announcements/2018/1/23/join-defna-board-member-recruitment/", "/blog/2018-01-23-join-defna-board-member-recruitment/"),
    ("/announcements/2018/9/6/semester-grants-report/", "/blog/2018-09-10-semester-grants-report/"),
    ("/announcements/2018/9/10/congratulations-jeff/", "/blog/2018-09-24-congratulations-jeff/"),
    ("/announcements/2020/03/02/board-updates/", "/blog/2020-03-02-board-updates/"),
    ("/announcements/2020/04/15/vendor-update/", "/blog/2020-04-15-vendor-update/"),
    ("/announcements/2020/10/21/djangoconus-video/", "/blog/2020-10-21-djangocon-us-2020-video/"),
    ("/announcements/2020/10/30/djangoconus-2020/", "/blog/2020-10-30-djangocon-us-2020/"),
    ("/announcements/2022/2/2/defna-board-member-recruitment/", "/blog/2022-02-02-defna-board-member-recruitment/"),
    ("/announcements/2022/5/10/djangoconus-2022-live/", "/blog/2022-05-10-djangoconus-2022-live/"),
    ("/announcements/2022/5/20/djangocon-us-call-for-venue-proposal-2023/", "/blog/2022-05-20-djangocon-us-call-for-venue-proposal-2023/"),
    ("/announcements/2023/01/01/call-for-proposals-for-djangocon-2023-website/", "/blog/2023-01-01-call-for-proposals-for-djangocon-2023-website/"),
    ("/announcements/2023/02/17/board-updates/", "/blog/2023-02-02-board-updates/"),
    ("/announcements/2023/07/24/board-updates/", "/blog/2023-07-24-board-updates/"),
    ("/announcements/2024/01/12/call-for-proposals-for-djangocon-2024-website/", "/blog/2024-01-12-call-for-proposals-for-djangocon-us-2024-website/"),
    ("/announcements/2024/01/17/djangoconus-2024-announced/", "/blog/2024-01-17-djangoconus-2024-announced/"),
    ("/announcements/2024/5/9/djangocon-us-call-for-venue-proposal-2025/", "/blog/2024-05-28-djangocon-us-call-for-venue-proposal-2025/"),
    ("/announcements/2024/10/16/djangocon-us-call-for-venue-proposal-2025-extension/", "/blog/2024-10-16-djangocon-us-call-for-venue-proposal-2025-extension/"),
    ("/announcements/2024/12/31/djangoconus-2025-announced/", "/blog/2024-12-31-djangoconus-2025-announced/"),
    ("/announcements/2025/9/10/djangocon-us-call-for-venue-proposal-2027/", "/blog/2025-09-10-call-for-venue-proposal-2027/"),
    ("/announcements/2025/07/21/celebrating-20-years-of-django/", "/blog/2025-07-21-celebrating-20-years-of-django/"),
    ("/announcements/2026/01/12/call-for-proposals-for-djangocon-2026-website/", "/blog/2026-01-12-call-for-proposals-for-djangocon-us-2026-website/"),
    ("/defna-board-member-update-july", "/blog/2025-07-18-defna-board-member-update-july/"),
    # Missing posts — redirect to blog index until they're added
    ("/announcements/2021/1/29/join-defna-board-member-recruitment/", "/blog/"),
    ("/announcements/2021/04/09/board-updates/", "/blog/"),
    ("/announcements/2022/11/5/defna-board-member-recruitment/", "/blog/"),
    ("/announcements/2023/05/01/board-updates/", "/blog/"),
    ("/announcements/2024/03/26/defna-board-member-recruitment/", "/blog/"),
    ("/announcements/2025/02/27/defna-board-member-recruitment/", "/blog/"),
    ("/announcements/2017/6/27/one-month-left-to-submit-djangocon-venue-proposals-for-2018-and-2019/", "/blog/"),
    # Old broken slugs → new correct slugs (for anyone who bookmarked the broken URLs)
    ("/blog/djangocon-us-2016-in-phillydjangocon-us-2016-in-ph/", "/blog/2016-02-10-djangocon-us-2016-in-philly/"),
    ("/blog/djangocon-us-call-for-venue-proposal-2017djangocon/", "/blog/2016-06-08-djangocon-us-call-for-venue-proposal-2017/"),
    ("/blog/defna-phase-iidefna-phase-ii/", "/blog/2016-07-20-defna-phase-ii/"),
    ("/blog/djangocon-us-2017-in-spokane-washingtondjangocon-u/", "/blog/2016-12-01-djangocon-us-2017-in-spokane-washington/"),
    ("/blog/defna-board-member-recruitment-join-usdefna-board-/", "/blog/2017-04-04-defna-board-member-recruitment-join-us/"),
    ("/blog/welcome-new-board-memberswelcome-new-board-members/", "/blog/2017-07-20-welcome-new-board-members/"),
    ("/blog/the-joys-of-catering-part-1-tickets-sold-does-nott/", "/blog/2017-08-01-the-joys-of-catering-part-1/"),
    ("/blog/call-for-proposals-for-djangocon-2018-websitecall-/", "/blog/2017-10-12-call-for-proposals-for-djangocon-2018-website/"),
    ("/blog/djangocon-us-2018-in-san-diegodjangocon-us-2018-in/", "/blog/2017-11-02-djangocon-us-2018-in-san-diego/"),
    ("/blog/join-defna-board-member-recruitmentjoin-defna-boar/", "/blog/2018-01-23-join-defna-board-member-recruitment/"),
    ("/blog/semester-grants-reportsemester-grants-report/", "/blog/2018-09-10-semester-grants-report/"),
    ("/blog/congratulations-jeffcongratulations-jeff/", "/blog/2018-09-24-congratulations-jeff/"),
    ("/blog/board-updatesboard-updates/", "/blog/2020-03-02-board-updates/"),
    ("/blog/vendor-updatevendor-update/", "/blog/2020-04-15-vendor-update/"),
    ("/blog/djangocon-us-2020-videodjangocon-us-2020-video/", "/blog/2020-10-21-djangocon-us-2020-video/"),
    ("/blog/djangocon-us-2020djangocon-us-2020/", "/blog/2020-10-30-djangocon-us-2020/"),
    ("/blog/join-defna-board-member-recruitmentdefna-board-mem/", "/blog/2022-02-02-defna-board-member-recruitment/"),
    ("/blog/djangocon-us-2022-is-livedjangoconus-2022-live/", "/blog/2022-05-10-djangoconus-2022-live/"),
    ("/blog/djangocon-us-call-for-venue-proposal-2023djangocon/", "/blog/2022-05-20-djangocon-us-call-for-venue-proposal-2023/"),
    ("/blog/call-for-proposals-for-djangocon-us-2023-websiteca/", "/blog/2023-01-01-call-for-proposals-for-djangocon-2023-website/"),
    ("/blog/board-member-update-for-2023board-updates/", "/blog/2023-02-02-board-updates/"),
    ("/blog/board-member-update-for-july-2023board-updates/", "/blog/2023-07-24-board-updates/"),
    ("/blog/call-for-proposals-for-djangocon-us-2024-websiteca/", "/blog/2024-01-12-call-for-proposals-for-djangocon-us-2024-website/"),
    ("/blog/djangocon-us-2024-has-been-announceddjangoconus-20/", "/blog/2024-01-17-djangoconus-2024-announced/"),
    ("/blog/board-member-update-for-may-2024board-updates/", "/blog/2024-05-01-board-updates/"),
    ("/blog/djangocon-us-call-for-venue-proposal-2025djangocon/", "/blog/2024-05-28-djangocon-us-call-for-venue-proposal-2025/"),
    ("/blog/djangocon-us-call-for-venue-proposal-2025-extensio/", "/blog/2024-10-16-djangocon-us-call-for-venue-proposal-2025-extension/"),
    ("/blog/djangocon-us-2025-has-been-announceddjangoconus-20/", "/blog/2024-12-31-djangoconus-2025-announced/"),
    ("/blog/board-member-update-for-20252025-07-18-defna-board/", "/blog/2025-07-18-defna-board-member-update-july/"),
    ("/blog/djangocon-us-call-for-venue-proposals-2027-28call-/", "/blog/2025-09-10-call-for-venue-proposal-2027/"),
    ("/blog/call-for-proposals-for-djangocon-us-2026-websiteca/", "/blog/2026-01-12-call-for-proposals-for-djangocon-us-2026-website/"),
    ("/blog/celebrating-20-years-of-django-looking-back-moving/", "/blog/2025-07-21-celebrating-20-years-of-django/"),
    # Page redirects
    ("/blm/", "/"),
    ("/home-alt/", "/"),
    ("/home-alt-2/", "/"),
]


def seed_redirects(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Redirect = apps.get_model("redirects", "Redirect")

    site = Site.objects.get_current()

    for old_path, new_path in REDIRECTS:
        Redirect.objects.get_or_create(
            site=site,
            old_path=old_path,
            defaults={"new_path": new_path},
        )


def unseed_redirects(apps, schema_editor):
    Redirect = apps.get_model("redirects", "Redirect")
    old_paths = [old for old, _ in REDIRECTS]
    Redirect.objects.filter(old_path__in=old_paths).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("redirects", "0002_alter_redirect_new_path_help_text"),
        ("sites", "0002_alter_domain_unique"),
        ("website", "0014_fix_doubled_blog_slugs"),
    ]

    operations = [
        migrations.RunPython(seed_redirects, unseed_redirects),
    ]
