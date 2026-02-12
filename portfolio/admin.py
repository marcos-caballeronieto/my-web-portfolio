from django.contrib import admin
from .models import Project, Category, Certificate

class ProjectAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Project model.

    - Displays 'title' and 'is_featured' fields in the list view.
    - Allows inline editing of the 'is_featured' field.
    - Uses horizontal filter widget for the 'categories' and 'related_projects' many-to-many fields.
    - Auto-generates slug from title.
    """
    list_display = ('title', 'slug', 'is_featured')
    list_editable = ('is_featured',)
    filter_horizontal = ('categories', 'related_projects')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    fieldsets = (
        ("General", {
            "fields": ("icon", "date", "url")
        }),
        ("English", {
            "fields": ("title_en", "subtitle_en", "description_en")
        }),
        ("Spanish", {
            "fields": ("title_es", "subtitle_es", "description_es")
        }),
        ("Legacy/Default", {
            "fields": ("title", "subtitle", "description")
        }),
    )