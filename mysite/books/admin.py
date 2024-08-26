# Register your models here.
from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('publication_date',) 

    search_fields = ["title"]

admin.site.register(Author)
admin.site.register(Book, BookAdmin)

