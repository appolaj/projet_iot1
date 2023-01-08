from . import views, api
from django.urls import path
urlpatterns = [
   path('',views.home,name='index'),
   path('csv', views.exp_csv, name='csv'),
   path('csv1', views.exp_csv1, name='csv1'),
   path('csv2', views.exp_csv2, name='csv2'),
   path('csv3', views.exp_csv3, name='csv3'),
   path('csv4', views.exp_csv4, name='csv4'),
   path('csv5', views.exp_csv5, name='csv5'),



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