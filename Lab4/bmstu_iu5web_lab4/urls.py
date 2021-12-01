from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ice_cream/<int:id>/', views.ice_cream, name='ice_cream')
]
