from .models import Puzzle
from django.contrib import admin


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('name', 'released_at', 'puzzle')


admin.site.register(Puzzle, PuzzleAdmin)
