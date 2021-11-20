from django.urls import path
from blog import views
urlpatterns = [
    path('', views.index),
    path('<slug:pk>/', views.article),
]
