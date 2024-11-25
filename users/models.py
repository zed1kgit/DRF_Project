from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    """User model."""
    username = models.CharField(_('username'), max_length=150, unique=True,)
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    first_name = models.CharField(max_length=150, verbose_name=_('first name'), **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name=_('last name'), **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name=_('phone number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('active'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['id']
