from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured')
    list_editable = ('is_featured',)

# Register your models here.

admin.site.register(Project, ProjectAdmin)