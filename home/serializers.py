from rest_framework import serializers
from home.models import *

class transSr(serializers.ModelSerializer):
    class Meta():
        model=trans
        fields=[
            "bike",
            "amt",
            "transaction"
        ]
class logSr(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
