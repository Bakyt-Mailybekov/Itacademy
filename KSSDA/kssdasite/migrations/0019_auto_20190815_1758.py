# Generated by Django 2.2.4 on 2019-08-15 11:58

from django.db import migrations, models
import django.db.models.deletion
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0018_auto_20190815_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='language_project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='kssdasite.Language'),
        ),
        migrations.AlterField(
            model_name='project',
            name='picture_project',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]
