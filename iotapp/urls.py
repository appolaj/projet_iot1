from . import views, api
from django.urls import path
urlpatterns = [
   path('index',views.home,name='index'),
   path('csv', views.exp_csv, name='csv'),
   path('graph', views.dht11, name='graph'),
   path('yesterday', views.dht12, name='yesterday'),
   path('lastweek', views.dhtlastweek, name='lastweek'),
path('day2', views.day2, name='day2'),
path('day3', views.day3, name='day3'),
path('day4', views.day4, name='day4'),
path('day5', views.day5, name='day5'),



##API
   path('api/list',api.Dlist, name="DHT11List"),

#genericviews
   path('api/post',api.Dhtviews.as_view(),name="DHT_post"),

]