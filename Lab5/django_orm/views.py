from django.shortcuts import render
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
