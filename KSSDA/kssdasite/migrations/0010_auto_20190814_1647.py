# Generated by Django 2.2.4 on 2019-08-14 10:47

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0009_auto_20190814_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture_project',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]
