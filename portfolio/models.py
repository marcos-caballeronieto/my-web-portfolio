from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Category(models.Model):
    """
    Represents a category for grouping projects.
    Each category has a unique name.
    """
    name = models.CharField(max_length=100, unique=True)
    is_main = models.BooleanField(default=False, help_text="Show as a prominent button instead of in the dropdown")
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    Represents a project in the portfolio.
    Includes details like title, description, images, URLs, and relevance.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    short_description = models.TextField(default='No description', blank=True)
    description = CKEditor5Field('Description', config_name='default')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='projects')
    related_projects = models.ManyToManyField('self', blank=True, symmetrical=True)
    is_miniproject = models.BooleanField(default=False, help_text="Mark this as a miniproject.")
    parent_project = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='miniprojects', help_text="If this is a miniproject, select its main parent project.")
    class Relevance(models.IntegerChoices):
        VERY_LOW = 1, 'Very Low'
        LOW = 2, 'Low'
        MEDIUM = 3, 'Medium'
        HIGH = 4, 'High'
        VERY_HIGH = 5, 'Very High'
    relevance = models.IntegerField(choices=Relevance.choices, default=Relevance.MEDIUM)

    class CoverType(models.TextChoices):
        IMAGE = 'IMAGE', 'Static Image'
        THREEJS = 'THREEJS', 'Three.js Animation'
        HTML = 'HTML', 'Raw HTML Code'
    
    cover_type = models.CharField(
        max_length=10, 
        choices=CoverType.choices, 
        default=CoverType.IMAGE,
        help_text="Select what type of content to display as the project cover in the detail view."
    )
    
    list_cover_type = models.CharField(
        max_length=10, 
        choices=CoverType.choices, 
        default=CoverType.IMAGE,
        verbose_name="List View Cover Type",
        help_text="Select what type of content to display in the project list (outside view)."
    )

    list_image = models.ImageField(
        upload_to='projects/list_covers/', 
        blank=True, 
        null=True,
        help_text="Optional: Different image for the list view. If empty, the main image is used."
    )
    
    threejs_script = models.TextField(
        blank=True, 
        null=True, 
        help_text="JavaScript code to initialize the Three.js scene (using a container with ID 'threejs-container-{{project.id}}')."
    )

    threejs_file = models.FileField(
        upload_to='projects/threejs/',
        blank=True,
        null=True,
        help_text="Upload a .js file for the Three.js initialization script. Takes precedence over the text field."
    )
    
    html_content = models.TextField(
        blank=True, 
        null=True, 
        help_text="Custom HTML/CSS to be rendered as the cover."
    )

    html_file = models.FileField(
        upload_to='projects/html/',
        blank=True,
        null=True,
        help_text="Upload an .html file for the custom cover content. Takes precedence over the text field."
    )

    list_html_content = models.TextField(
        blank=True, 
        null=True, 
        help_text="Custom HTML/CSS for the list view cover."
    )

    list_html_file = models.FileField(
        upload_to='projects/html/',
        blank=True,
        null=True,
        help_text="Upload an .html file for the list view cover. Takes precedence over the text field."
    )

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        
        # If detail cover_type is IMAGE, we must have image.
        if self.cover_type == self.CoverType.IMAGE and not self.image:
            raise ValidationError({
                'image': 'Image is required when Detail View Cover Type is Static Image.'
            })
            
        # If list_cover_type is IMAGE, we must have either list_image or image.
        if self.list_cover_type == self.CoverType.IMAGE and not self.list_image and not self.image:
            raise ValidationError({
                'image': 'Image (or List View Cover Image) is required when List View Cover Type is Static Image.'
            })

    def __str__(self):
        return self.title
    
    def get_threejs_script(self):
        """Returns script content from file if exists, otherwise from text field."""
        if self.threejs_file:
            try:
                with self.threejs_file.open('r') as f:
                    return f.read()
            except Exception as e:
                return f"// Error reading Three.js file: {e}"
        return self.threejs_script
    
    def get_html_content(self):
        """Returns HTML content from file if exists, otherwise from text field."""
        if self.html_file:
            try:
                with self.html_file.open('r') as f:
                    return f.read()
            except Exception as e:
                return f"<!-- Error reading HTML file: {e} -->"
        return self.html_content
        
    def get_list_html_content(self):
        """Returns List View HTML content from file if exists, otherwise from text field."""
        if self.list_html_file:
            try:
                with self.list_html_file.open('r') as f:
                    return f.read()
            except Exception as e:
                return f"<!-- Error reading List HTML file: {e} -->"
        return self.list_html_content
    

class ProjectDescriptionImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='description_images',
    )
    image = models.ImageField(upload_to='projects/descriptions/')
    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.project.title} description image"


class CertificateCategory(models.Model):
    """
    Represents a category for grouping certificates and courses.
    Supports bilingual names and ordering/display prominence.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Name (Default/EN)")
    name_en = models.CharField(max_length=100, blank=True, verbose_name="Name (EN)")
    name_es = models.CharField(max_length=100, blank=True, verbose_name="Name (ES)")
    is_main = models.BooleanField(default=True, help_text="Show as a prominent button instead of in the dropdown")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Certificate / Course Category"
        verbose_name_plural = "Certificate / Course Categories"

    def __str__(self):
        return self.name_en or self.name_es or self.name


class Certificate(models.Model):
    """
    Represents a certificate, course, or achievement.
    Includes icon, title, subtitle, description, date, categories, visibility, and optional URL.
    """
    class ItemType(models.TextChoices):
        CERTIFICATE = 'CERTIFICATE', 'Certificate'
        COURSE = 'COURSE', 'Course'

    item_type = models.CharField(
        max_length=20,
        choices=ItemType.choices,
        default=ItemType.CERTIFICATE,
        verbose_name="Type"
    )
    icon = models.CharField(max_length=10, default='📜', verbose_name="Icon/Emoji")
    icon_file = models.FileField(upload_to='certificates/icons/', blank=True, null=True, verbose_name="Icon SVG/PNG")
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle / Organization")
    description = CKEditor5Field(verbose_name="Description", config_name='default')
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Title (EN)")
    title_es = models.CharField(max_length=200, blank=True, verbose_name="Title (ES)")
    subtitle_en = models.CharField(max_length=200, blank=True, verbose_name="Subtitle / Organization (EN)")
    subtitle_es = models.CharField(max_length=200, blank=True, verbose_name="Subtitle / Organization (ES)")
    description_en = CKEditor5Field(verbose_name="Description (EN)", config_name='default', blank=True)
    description_es = CKEditor5Field(verbose_name="Description (ES)", config_name='default', blank=True)
    date = models.DateField(verbose_name="Date Obtained")
    url = models.URLField(blank=True, null=True, verbose_name="Link (Optional)")
    categories = models.ManyToManyField(
        CertificateCategory,
        blank=True,
        related_name='certificates',
        verbose_name="Categories"
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_visible = models.BooleanField(default=True, verbose_name="Visible", help_text="Show this item on the portfolio")
    show_on_about = models.BooleanField(default=True, verbose_name="Show on About Me", help_text="Display in the About Me summary section")

    class Meta:
        ordering = ['order', '-date']
        verbose_name = "Certificate / Course"
        verbose_name_plural = "Certificates & Courses"

    def __str__(self):
        return self.title_en or self.title_es or self.title


class SkillCategory(models.Model):
    """
    Represents a category for organizing technical and domain skills.
    Supports bilingual names/descriptions, icons, ordering, and visibility.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Name (Default/EN)")
    name_en = models.CharField(max_length=100, blank=True, verbose_name="Name (EN)")
    name_es = models.CharField(max_length=100, blank=True, verbose_name="Name (ES)")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    description_es = models.TextField(blank=True, verbose_name="Description (ES)")
    icon = models.CharField(
        max_length=100,
        default='fas fa-tools',
        verbose_name="FontAwesome Icon Class or Emoji",
        help_text="e.g. 'fas fa-brain', 'fas fa-robot'"
    )
    icon_file = models.FileField(upload_to='skills/category_icons/', blank=True, null=True, verbose_name="Icon SVG/PNG")
    is_main = models.BooleanField(default=True, help_text="Show as a prominent button instead of in the dropdown")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_visible = models.BooleanField(default=True, verbose_name="Visible")
    show_on_about = models.BooleanField(default=True, verbose_name="Show on About Me", help_text="Display this category in the About Me summary section")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name_en or self.name_es or self.name


class Skill(models.Model):
    """
    Represents an individual skill belonging to a SkillCategory.
    Supports bilingual names/descriptions, optional icon/URL, ordering, and visibility.
    """
    name = models.CharField(max_length=100, verbose_name="Skill Name (Default/EN)")
    name_en = models.CharField(max_length=100, blank=True, verbose_name="Skill Name (EN)")
    name_es = models.CharField(max_length=100, blank=True, verbose_name="Skill Name (ES)")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    description_es = models.TextField(blank=True, verbose_name="Description (ES)")
    icon = models.CharField(max_length=100, blank=True, verbose_name="FontAwesome Icon Class or Emoji")
    icon_file = models.FileField(upload_to='skills/icons/', blank=True, null=True, verbose_name="Icon SVG/PNG")
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills',
        verbose_name="Category"
    )
    url = models.URLField(blank=True, null=True, verbose_name="Link (Optional)")
    order = models.PositiveIntegerField(default=0, help_text="Display order within category (lower numbers appear first)")
    is_visible = models.BooleanField(default=True, verbose_name="Visible")
    show_on_about = models.BooleanField(default=True, verbose_name="Show on About Me")

    class Meta:
        ordering = ['category__order', 'order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name_en or self.name_es or self.name
    
