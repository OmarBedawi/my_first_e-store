from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ebooks, name='ebooks'),
    path('ebook_detail/<int:ebook_id>/', views.ebook_detail, name='ebook_detail'),
    path('add_ebook/', views.add_ebook, name='add_ebook'),
    path('edit_ebook/<int:ebook_id>/', views.edit_ebook, name='edit_ebook'),
    path('delete_ebook/<int:ebook_id>/', views.delete_ebook, name='delete_ebook'),
    path('ebook_reader/', views.ebook_reader, name='ebook_reader'),
    path('ebook_reader_detail/<int:ebook_reader_id>/', views.ebook_reader_detail, name='ebook_reader_detail'),
    path('add_ebook_reader/', views.add_ebook_reader, name='add_ebook_reader'),
    path('edit_ebook_reader/<int:ebook_reader_id>/', views.edit_ebook_reader, name='edit_ebook_reader'),
    path('delete_ebook_reader/<int:ebook_reader_id>/', views.delete_ebook_reader, name='delete_ebook_reader'),
]
