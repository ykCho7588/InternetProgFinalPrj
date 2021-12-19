from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_item_page),
    # path('', views.index),
    path('search/<str:q>/', views.ItemSearch.as_view()),
    path('update_item/<int:pk>/', views.ItemUpdate.as_view()),
    path('create_item/', views.ItemCreate.as_view()),
    path('category/<str:slug>', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('', views.ItemList.as_view()),
]