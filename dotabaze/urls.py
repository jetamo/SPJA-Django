"""dotabaze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Dota.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroes/', Dota.views.heroes, name='heroes'),
    path('hero/<int:hero_id>/', Dota.views.hero_index, name='hero_index'),
    path('heroes/search/', Dota.views.atribute_search, name='heroes_search'),
    path('tips/<int:tip_id>/', Dota.views.comments, name='comments'),
    path('hero/<int:hero_id>/add_tip/', Dota.views.AddTip, name='addTip'),
    path('tips/<int:tip_id>/add_comment/', Dota.views.AddComment, name='addComment'),

]
