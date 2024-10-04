from django.urls import path
from . import views

urlpatterns = [
    path('glyco/excel', views.convert_glyco_excel, name='glyco'),
    path('', views.index)
]
