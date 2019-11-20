from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'isbn_number']
    list_filter = ['name']
    search_fields = ['name']
