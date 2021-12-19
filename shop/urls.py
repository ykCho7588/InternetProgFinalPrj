from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_item_page),
    # path('', views.index),
    path('create_item/', views.ItemCreate.as_view()),
    path('category/<str:slug>', views.category_page),
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('', views.ItemList.as_view()),
]