# Generated by Django 4.0.6 on 2022-07-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_team_facebook_link_alter_team_google_plus_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='google_plus_link',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(max_length=100),
        ),
    ]
