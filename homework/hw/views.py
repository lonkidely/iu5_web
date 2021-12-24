from django.shortcuts import render
from .models import Opers, Langs

# Create your views here.

def report(request):
    return render(request, 'report.html', {'data':{'opers':Opers.objects.select_related('lang').order_by('lang__title')}})