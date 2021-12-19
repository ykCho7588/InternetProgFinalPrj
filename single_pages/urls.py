from django.urls import path

from . import views


urlpatterns = [ #서버IP/
    path('', views.landing), #서버IP/
    path('about_us/', views.about_us), #서버IP/about_us/
    path('my_page/', views.my_page) #서버IP/my_page/
]