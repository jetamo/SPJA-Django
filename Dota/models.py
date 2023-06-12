from django.db import models

class Hero(models.Model):
    atributes = [
        ("Intelligence", "Intelligence"),
        ("Agility", "Agility"),
        ("Strength", "Strength")
    ]
    name = models.CharField(max_length = 30)
    hero_img_url = models.CharField(max_length = 300)
    primary_atribute = models.CharField(max_length=30, choices=atributes)
    def __str__(self):
        return ("{}".format(self.name))

class Tip(models.Model):
    title = models.CharField(max_length = 45)
    text = models.TextField(help_text='Type you tip here')
    hero = models.ForeignKey('Hero', on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    text = models.TextField()
    tip = models.ForeignKey('Tip', on_delete = models.CASCADE)


# Create your models here.
