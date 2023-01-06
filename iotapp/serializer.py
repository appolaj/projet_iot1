from rest_framework import serializers
from .models import Dht
#serializers define the API represantation
class ser(serializers.ModelSerializer):
    class Meta :
        model = Dht
        fields = ['id', 'temp','hum','dt']
