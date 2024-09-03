from django.contrib import admin

from notes.models import Note


# Register your models here.

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
    search_fields = ('title', 'user__username')
