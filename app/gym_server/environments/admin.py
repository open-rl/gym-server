from django.contrib import admin
from environments.models import Environment


# Register your models here.
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'video_url')
    fields = ('name', 'description', 'video_url')


admin.site.register(Environment, EnvironmentAdmin)
