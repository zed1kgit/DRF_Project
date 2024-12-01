from django.db import models
from users.models import NULLABLE
from django.utils.translation import gettext_lazy as _

class Section(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
        ordering = ['id']

class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('section'))
    title = models.CharField(max_length=150, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('section content')
        verbose_name_plural = _('section contents')
        ordering = ['id']
