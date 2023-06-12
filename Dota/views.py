from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Dota.models import Hero, Tip, Comment
from Dota.forms import AtributeSearch, addTip, addComment

def heroes(request):
    heroes = Hero.objects.all().order_by('name')
    return render(request, 'heroes.html', {'heroes':heroes})

def hero_index(request, hero_id):
    hero = get_object_or_404(Hero, id = hero_id)
    tips = Tip.objects.filter(hero = hero)
    return render(request, 'hero_index.html', {'hero':hero, 'tips':tips})

def atribute_search(request):
    if request.method == 'POST':
        form = AtributeSearch(request.POST)
        if form.is_valid():
            atribute = form.cleaned_data['atribute']
            heroes = Hero.objects.filter(primary_atribute = atribute)
        else:
            heroes = None
    else:
        heroes = None
        form = AtributeSearch()
    return render(request, 'atribute_search.html', {'form':form, 'heroes':heroes})

def comments(request, tip_id):
    tip = get_object_or_404(Tip, id = tip_id)
    comments = Comment.objects.filter(tip = tip)
    return render(request, 'comments.html', {'tip':tip, 'comments':comments})

def AddTip(request, hero_id):
    hero = Hero.objects.get(id=hero_id)
    if request.method == 'POST':
        form = addTip(request.POST, initial={'hero':hero.pk, 'likes':0})
        if form.is_valid():
            form.save()
    else:
        form = addTip()
    return render(request, 'addTip.html', {'form':form, 'hero_id':hero_id})
    
def AddComment(request, tip_id):
    tip = Tip.objects.get(id=tip_id)
    if request.method == 'POST':
        form = addComment(request.POST, initial={'tip':tip.pk})
        if form.is_valid():
            form.save()
    else:
        form = addComment()
    return render(request, 'addComment.html', {'form':form, 'tip_id':tip_id})

# Create your views here.
