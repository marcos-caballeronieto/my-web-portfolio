from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Project,
    ProjectDescriptionImage,
    Category,
    Certificate,
    CertificateCategory,
    SkillCategory,
    Skill,
)


class ProjectDescriptionImageInline(admin.TabularInline):
    model = ProjectDescriptionImage
    extra = 1
    fields = ('image', 'alt_text', 'markdown_reference')
    readonly_fields = ('markdown_reference',)
    verbose_name = "Description image"
    verbose_name_plural = "Description images"
    description = "Upload and save images here. Copy the Markdown reference into the project description."

    @admin.display(description="Markdown reference")
    def markdown_reference(self, obj):
        if not obj or not obj.image:
            return "-"
        alt_text = obj.alt_text or "Image"
        return format_html('![{}]({})', alt_text, obj.image.url)


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
    inlines = [ProjectDescriptionImageInline]
    
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "short_description", "description", "categories", "is_featured", "relevance"),
            "description": "Add images in the Description images section below and copy their Markdown references into the description. Use a Markdown code block for tables; they display in a horizontally scrollable layout on small screens."
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

class CertificateCategoryInline(admin.TabularInline):
    model = Certificate.categories.through
    extra = 1
    verbose_name = "Certificate / Course"
    verbose_name_plural = "Certificates & Courses"


@admin.register(CertificateCategory)
class CertificateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'name_es', 'is_main', 'order')
    list_editable = ('is_main', 'order')
    search_fields = ('name', 'name_en', 'name_es')
    inlines = [CertificateCategoryInline]


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_type', 'display_categories', 'date', 'order', 'is_visible', 'show_on_about')
    list_editable = ('item_type', 'order', 'is_visible', 'show_on_about')
    list_filter = ('item_type', 'is_visible', 'show_on_about', 'categories')
    search_fields = ('title', 'title_en', 'title_es', 'subtitle', 'subtitle_en', 'subtitle_es')
    filter_horizontal = ('categories',)

    @admin.display(description="Categories")
    def display_categories(self, obj):
        return ", ".join(str(c) for c in obj.categories.all()) or "-"
    fieldsets = (
        ("General", {
            "fields": (
                "item_type",
                "icon",
                "icon_file",
                "date",
                "url",
                "categories",
                "order",
                "is_visible",
                "show_on_about",
            )
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


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'name_en', 'name_es', 'icon', 'order', 'is_visible', 'show_on_about')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'name_es', 'icon', 'is_main', 'order', 'is_visible', 'show_on_about')
    list_editable = ('is_main', 'order', 'is_visible', 'show_on_about')
    list_filter = ('is_main', 'is_visible', 'show_on_about')
    search_fields = ('name', 'name_en', 'name_es')
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'name_en', 'name_es', 'order', 'is_visible', 'show_on_about')
    list_editable = ('order', 'is_visible', 'show_on_about')
    list_filter = ('category', 'is_visible', 'show_on_about')
    search_fields = ('name', 'name_en', 'name_es', 'description_en', 'description_es')