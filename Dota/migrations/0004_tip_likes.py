# Generated by Django 2.2.7 on 2019-12-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0003_auto_20191213_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
