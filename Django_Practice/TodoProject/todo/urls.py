from typing import List
from django.urls import path
from django.urls import path
from .views import TodoDelete, TodoList, TodoDetail, TodoCreate, TodoUpdate

urlpatterns = [
    path('list/',TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='crete'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
]
