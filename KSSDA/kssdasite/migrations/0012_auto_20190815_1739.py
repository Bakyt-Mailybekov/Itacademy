# Generated by Django 2.2.4 on 2019-08-15 11:39

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0011_auto_20190814_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture_project',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=50),
        ),
    ]
