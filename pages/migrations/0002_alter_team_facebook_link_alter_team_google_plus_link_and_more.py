# Generated by Django 4.0.6 on 2022-07-08 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='google_plus_link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.CharField(max_length=100),
        ),
    ]
