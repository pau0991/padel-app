from django.urls import path
from core import views

# define the urls
urlpatterns = [
    path('users/', views.users),
    path('users/<int:pk>/', views.user_detail),
    path('matches/', views.matches),
    path('matches/<int:pk>/', views.match_detail),
]