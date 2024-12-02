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


class Tests(models.Model):
    test_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('test section'))
    description = models.TextField(verbose_name=_('description'), **NULLABLE)
    question = models.TextField(verbose_name=_('question'), **NULLABLE)
    answer = models.TextField(max_length=40, verbose_name=_('answer'), **NULLABLE)

    def __str__(self):
        return f'Тест по курсу {self.test_section.title}'

    class Meta:
        verbose_name = _('test')
        verbose_name_plural = _('tests')
        ordering = ['test_section']
