# Generated by Django 3.0.5 on 2020-06-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreadsheets',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]