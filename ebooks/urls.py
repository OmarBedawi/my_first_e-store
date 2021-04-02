from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ebooks, name='ebooks'),
    path('<int:ebook_id>/', views.ebook_detail, name='ebook_detail'),
    path('add/', views.add_ebook, name='add_ebook'),
    path('edit/<int:ebook_id>/', views.edit_ebook, name='edit_ebook'),
    path('delete/<int:ebook_id>/', views.delete_ebook, name='delete_ebook'),
    path('ebook_reader/', views.ebook_reader, name='ebook_reader'),
    path('<int:ebook_reader_id>/', views.ebook_reader_detail, name='ebook_reader_detail'),
]
