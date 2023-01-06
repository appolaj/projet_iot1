from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dht
from .serializer import ser


@api_view(['GET'])
def Dlist(request):
    all_data = Dht.objects.all()
    data = ser(all_data, many=True).data
    return Response({'data': data})
class Dhtviews(generics.CreateAPIView):
    queryset = Dht.objects.all()
    serializer_class = ser
