from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'world_data/(?P<category>\w*)', views.world_data),
    url(r'nation_data/(?P<code>\w+)/', views.nation_data),
    url(r'most_popular/', views.most_popular_torrent),
]
