from .models import Operator, Proglang
from rest_framework import serializers


class OperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ["id", "name", "count_cycles"]


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proglang
        fields = ["id", "title"]
