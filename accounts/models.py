from django.db import models


# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

import os
from django.conf import settings


class AccountManager(BaseUserManager):
    """ Method for account model
    """
    def create_user(self, email, password=None, **kwargs):

        if not email:
            raise ValueError("Users must have a valid email address.")
        if not kwargs.get("username"):
            raise ValueError("Users must have a valid username.")

        account = self.model(email=self.normalize_email(email), username=kwargs.get("username"))
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        """ method that creates a user that has Administrative
            access. (can access the admin panel)
        """
        account = self.create_user(email, password, **kwargs)
        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True

        account.save()

        return account


class Account(AbstractBaseUser,PermissionsMixin):
    """ Custom model for the users. it extends to
        the `django.auth.models.User`
    """
    email = models.EmailField(_("Email"), max_length=225, unique=True)
    username = models.CharField(max_length=225, unique=True)
    full_name = models.CharField(_("Full name"), max_length=225, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_activated = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_("Designates whether this user should be treated as "
                    "active. Unselect this instead of deleting accounts."))

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return "{email}".format(email=self.email)

    def get_short_name(self):
        return "{}".format((self.email).split('@')[0])

    def email_as_username(self):
        """ extract username from email
        """
        return "{username}".format(username=self.email)
