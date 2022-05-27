from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add', views.add, name='add'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.deleteitem, name='deleteitem'),
    path('movies', views.movies, name='movies'),
    # path('api/createproducts', views.createproduct, name='createproduct'),
   
]
