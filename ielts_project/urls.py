from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]

handler404 = 'books.views.custom_page_not_found_view'
handler500 = 'books.views.custom_error_view'
