from django.urls import path
from . import views


urlpatterns =[
    path('hearse/<int:user_id>/', views.hearses, name="hearses"),
    path('show_pdf', views.show_pdf, name='show_details'),
    path('index/<int:user_id>/', views.request_data, name='index'),
]


