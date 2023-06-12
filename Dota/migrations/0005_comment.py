# Generated by Django 2.2.7 on 2019-12-13 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0004_tip_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dota.Tip')),
            ],
        ),
    ]
