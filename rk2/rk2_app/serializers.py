from .models import Langs, Opers
from rest_framework import serializers


class OperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opers
        fields = "__all__"


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langs
        fields = "__all__"
