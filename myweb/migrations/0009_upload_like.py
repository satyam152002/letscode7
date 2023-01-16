# Generated by Django 3.0.5 on 2020-09-12 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myweb', '0008_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]