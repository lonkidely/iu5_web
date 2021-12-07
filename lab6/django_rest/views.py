from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OperSerializer, LangSerializer
from .models import Operator, Proglang


# Create your views here.
def index(request):
    return render(request, 'index.html')


def opers(request):
    opers = Operator.objects.all()
    return render(request, 'operators.html', {'opers': opers})


def langs(request):
    langs = Proglang.objects.all()
    return render(request, 'proglangs.html', {'langs': langs})


def oper(request, id):
    oper = Operator.objects.get(id=id)
    return render(request, 'operator.html', {'oper': oper})


def lang(request, id):
    lang = Proglang.objects.get(id=id)
    return render(request, 'proglang.html', {'lang': lang})


class OperViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all().order_by("name")
    serializer_class = OperSerializer


class LangViewSet(viewsets.ModelViewSet):
    queryset = Proglang.objects.all().order_by("title")
    serializer_class = LangSerializer
