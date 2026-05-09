from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse

from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class StaffOnlySocialAccountAdapter(DefaultSocialAccountAdapter):
    """Restrict GitHub OAuth to pre-existing staff users only."""

    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            if not sociallogin.user.is_staff:
                raise ImmediateHttpResponse(self._denied_redirect())
            return

        # New social login — only allow if a staff user with this email exists
        email = (sociallogin.user.email or "").strip().lower()
        if not email:
            raise ImmediateHttpResponse(self._denied_redirect())

        User = get_user_model()
        try:
            user = User.objects.get(email__iexact=email, is_staff=True)
        except User.DoesNotExist:
            raise ImmediateHttpResponse(self._denied_redirect())

        sociallogin.connect(request, user)

    def _denied_redirect(self):
        url = reverse("admin:login") + "?error=unauthorized"
        return redirect(url)
