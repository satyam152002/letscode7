# Generated by Django 3.0.5 on 2020-09-12 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myweb', '0004_auto_20200910_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='liked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]