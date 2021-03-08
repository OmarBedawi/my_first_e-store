from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ebooks, name='ebooks'),
    path('<int:ebook_id>/', views.ebook_detail, name='ebook_detail'),
    path('add/', views.add_ebook, name='add_ebook'),
]
