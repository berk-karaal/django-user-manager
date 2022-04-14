import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_email_domain(email):
    """
    Validate that the domain of the given email address is in the
    ALLOWED_EMAIL_DOMAINS list in the settings.
    It won't check if the ALLOWED_EMAIL_DOMAINS equals to "*".
    """
    if not settings.ALLOWED_EMAIL_DOMAINS == "*":
        match = re.search(r"@([\w\.-]+)", email)  # get domain name with tld
        if not match:
            raise ValidationError(
                _("Couldn't find a domain name in '%(email)'"),
                params={"email": email},
            )

        domain = match.group(1)

        if not domain in settings.ALLOWED_EMAIL_DOMAINS:
            raise ValidationError(
                _(f"'{email}' is not in the ALLOWED_EMAIL_DOMAINS list."),
                params={"email": email},
            )
