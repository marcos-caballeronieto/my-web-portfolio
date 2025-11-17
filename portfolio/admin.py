from django.contrib import admin
from .models import Project, Category

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured')
    list_editable = ('is_featured',)
    filter_horizontal = ('categories',)

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)