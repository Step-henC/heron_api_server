from django.urls import path
from . import views

urlpatterns = [
    path('api/glyco/excel', views.convert_glyco_excel, name='glyco')
]
