"""
WSGI config for dev_defna_org project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

from django.conf import settings  # noqa: E402
from whitenoise import WhiteNoise  # noqa: E402

application = WhiteNoise(application, root=settings.STATIC_ROOT, prefix="static/")
application.add_files(settings.MEDIA_ROOT, prefix="media/")
