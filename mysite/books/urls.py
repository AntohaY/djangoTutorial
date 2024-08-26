from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]