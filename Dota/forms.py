from django import forms
from django.forms import ModelForm
from Dota.models import Hero, Tip, Comment

class AtributeSearch(forms.Form):
    OPTIONS = (
    ("Intelligence", "Intelligence"),
    ("Strength", "Strength"),
    ("Agility", "Agility"),
    )
    atribute = forms.ChoiceField(choices=OPTIONS)

class addTip(ModelForm):
    hero = forms.ModelChoiceField(queryset=Hero.objects.all(), disabled=True)
    class Meta:
        model = Tip
        fields = ['hero', 'title', 'text']

class addComment(ModelForm):
    tip = forms.ModelChoiceField(queryset=Tip.objects.all(), disabled=True)
    class Meta:
        model = Comment
        fields = ['tip', 'text']