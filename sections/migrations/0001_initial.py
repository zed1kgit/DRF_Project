# Generated by Django 5.0.9 on 2024-12-01 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SectionContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.section', verbose_name='section')),
            ],
            options={
                'verbose_name': 'section content',
                'verbose_name_plural': 'section contents',
                'ordering': ['id'],
            },
        ),
    ]
