from django.contrib import admin

from main.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'file'
    )
