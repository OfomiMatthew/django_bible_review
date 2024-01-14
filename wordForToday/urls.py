from django.urls import path 
from . import views

urlpatterns =[
  path('verse/', views.fetchData,name='verse'),
]