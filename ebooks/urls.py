from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ebooks, name='ebooks'),
    path('<ebook_id>', views.ebook_detail, name='ebook_detail'),
]
