from django.urls import path
from django_orm import views

urlpatterns = [
    path('', views.index),
    path('opers/', views.opers),
    path('langs/', views.langs),
    path('oper/<int:id>/', views.oper),
    path('lang/<int:id>/', views.lang),
]
