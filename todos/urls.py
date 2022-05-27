from django.urls import path
from todos import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('alltodos', views.alltodos, name='alltodos'),
    path('delete/<int:id>', views.delete, name='delete'),
]