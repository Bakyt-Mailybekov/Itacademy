# Generated by Django 2.2.4 on 2019-08-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0003_auto_20190807_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='picture_alumni',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='email_alumni',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='github_link_alumni',
            field=models.URLField(blank=True, null=True),
        ),
    ]
