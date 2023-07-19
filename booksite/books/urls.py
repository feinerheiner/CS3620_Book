from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='library'),
    path('books/<int:item_id>', views.book_detail, name='detail')
]
