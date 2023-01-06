from . import views, api
from django.urls import path
urlpatterns = [
   path('index',views.home,name='index'),
   #path('data', views.dht11, name='Data'),
   path('graph', views.dht11, name='graph'),
   path('yesterday', views.dht12, name='yesterday'),


##API
   path('api/list',api.Dlist, name="DHT11List"),

#genericviews
   path('api/post',api.Dhtviews.as_view(),name="DHT_post"),

]