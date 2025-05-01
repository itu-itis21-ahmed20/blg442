from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('token-game/', views.token_game, name='token_game'),  
]