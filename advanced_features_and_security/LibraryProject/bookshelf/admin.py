from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Show these fields in the list view
    list_filter = ('author',)            # Add sidebar filters
    search_fields = ('title', 'author')                     # Enable search by title and author

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  # Add custom fields
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  # Add custom fields to add form
    )
admin.site.register(CustomUser)