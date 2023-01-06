from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
    #return HttpResponse('bonjour à tous')
from django.shortcuts import render
# Create your views here.
from .models import Dht
def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab[len(tab)-37:len(tab)-1]}
    return render(request, 'graph.html', s)

def dht12(request):
    yes = Dht.objects.all()
    s1 = {'yes': yes[len(yes)-146:len(yes)-73]}
    return render(request, 'yesterday.html', s1)