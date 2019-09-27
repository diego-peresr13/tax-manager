from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from apps.rooms import views as views_rooms
from apps.books import views as views_book
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views_book.book_list, name='book_list'),
    path('books/create/', views_book.book_create, name='book_create'),
    path('books/update/<pk>', views_book.book_update, name='book_update'),
    path('books/delete/<pk>', views_book.book_delete, name='book_delete'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()