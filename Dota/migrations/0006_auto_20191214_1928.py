# Generated by Django 2.2.7 on 2019-12-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='primary_atribute',
            field=models.CharField(choices=[('Intelligence', 'Intelligence'), ('Agility', 'Agility'), ('Strength', 'Strength')], max_length=30),
        ),
    ]
