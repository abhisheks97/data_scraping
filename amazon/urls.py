from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.amazon_search, name='Get results from amazon according to searching keyword'),

]
