from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('snakes/', views.snakes_index, name='index'),
    path('snakes/<int:snake_id>/', views.snakes_detail, name='detail'),
]
