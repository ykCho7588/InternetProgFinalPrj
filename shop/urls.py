from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_item_page),
    path('', views.index),

]