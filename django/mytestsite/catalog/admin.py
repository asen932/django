from django.contrib import admin

# Register your models here.

from .models import Author, Book, BookInstance, Genre

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)

admin.site.register(Genre)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

admin.site.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


