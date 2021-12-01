from django.shortcuts import render
from .models import IceCream


# Create your views here.

def index(request):
    return render(request, '../templates/bmstu_iu5web_lab4/index.html', {'navbar': [
        {'title': 'Первый вид мороженого', 'id': '1'},
        {'title': 'Второй вид мороженого', 'id': '2'},
        {'title': 'Третий вид мороженого', 'id': '3'}
    ]})


def ice_cream(request, id):
    icecream = IceCream.objects.get(id=id)
    return render(request, '../templates/bmstu_iu5web_lab4/ice_cream.html', {'ice_cream':icecream})
