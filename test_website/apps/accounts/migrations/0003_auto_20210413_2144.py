# Generated by Django 3.1.7 on 2021-04-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210404_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook_url',
            field=models.URLField(blank=True, max_length=640, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin_url',
            field=models.URLField(blank=True, max_length=640, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter_url',
            field=models.URLField(blank=True, max_length=640, null=True),
        ),
    ]
