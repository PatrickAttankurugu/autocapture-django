from django.urls import path
from . import views

app_name = 'ghana_card_detector'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/verify/', views.verify_card, name='verify_card'),
]