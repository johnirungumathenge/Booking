from django.urls import path
from . import views
from hearse.views import Hearse

urlpatterns =[
    path('home/', views.home, name="home"),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name="logout"),
    path('show/<int:user_id>', views.show, name="show"),
    # path('hearse/<int:user_id>', views.hearses, name='hearse'),   
    path('show_request/<int:user_id>', views.show_request, name='show_request'),
]