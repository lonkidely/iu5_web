from django.shortcuts import render
from rest_framework import viewsets
from .models import Opers, Langs
from .serializers import OperSerializer, LangSerializer


# Create your views here.
class LangViewSet(viewsets.ModelViewSet):
    queryset = Langs.objects.all()
    serializer_class = LangSerializer


class OperViewSet(viewsets.ModelViewSet):
    queryset = Opers.objects.all()
    serializer_class = OperSerializer


def report(request):
    return render(request, 'report.html', {'data':{'opers':Opers.objects.select_related('lang')}})
