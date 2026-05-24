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
    list_display = ('title', 'slug', 'is_featured', 'cover_type', 'is_miniproject')
    list_editable = ('is_featured', 'is_miniproject')
    filter_horizontal = ('categories', 'related_projects')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "short_description", "description", "categories", "is_featured", "relevance")
        }),
        ("Miniproject Settings", {
            "fields": ("is_miniproject", "parent_project"),
            "description": "Specify if this project is a miniproject and link it to its parent project."
        }),
        ("Detail View Cover", {
            "fields": ("cover_type", "image", "threejs_script", "threejs_file", "html_content", "html_file"),
            "description": "Select the cover type and provide the corresponding content/script via text or file upload for the detail view."
        }),
        ("List View Cover (Outside)", {
            "fields": ("list_cover_type", "list_image", "list_html_content", "list_html_file"),
            "description": "Select the cover type and content to display in the project list or home page."
        }),
        ("URLs & Relations", {
            "fields": ("url", "github_url", "related_projects")
        }),
    )

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    fieldsets = (
        ("General", {
            "fields": ("icon", "icon_file", "date", "url")
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