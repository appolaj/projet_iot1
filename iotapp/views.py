from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
    #return HttpResponse('bonjour à tous')
from django.shortcuts import render
# Create your views here.
from .models import Dht
def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab[len(tab)-36:len(tab)]}
    return render(request, 'graph.html', s)

def dht12(request):
    yes = Dht.objects.all()
    s1 = {'yes': yes[len(yes)-146:len(yes)-73]}
    return render(request, 'yesterday.html', s1)

def exp_csv(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])

    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response

def dhtlastweek(request):

    return render(request, 'lastweek.html')


def day2(request):
    da2 = Dht.objects.all()
    d2 = {'da2': da2[len(da2)-219:len(da2)-147]}
    return render(request, 'day2.html', d2)

def day3(request):
    da3 = Dht.objects.all()
    d3 = {'da3': da3[len(da3)-292:len(da3)-220]}
    return render(request, 'day3.html', d3)


def day4(request):
    da4 = Dht.objects.all()
    d4 = {'da4': da4[len(da4)-365:len(da4)-293]}
    return render(request, 'day4.html', d4)

def day5(request):
    da5 = Dht.objects.all()
    d5 = {'da5': da5[len(da5)-438:len(da5)-366]}
    return render(request, 'day5.html', d5)

