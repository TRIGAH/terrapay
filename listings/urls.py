from django.urls import path
from . import views

urlpatterns = [
    path('', views.land_list, name='land_list'),
    path('land/<int:pk>/', views.land_detail, name='land_detail'),
]
