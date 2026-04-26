from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Category(models.Model):
    """
    Represents a category for grouping projects.
    Each category has a unique name.
    """
    name = models.CharField(max_length=100, unique=True)
    
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
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='projects')
    related_projects = models.ManyToManyField('self', blank=True, symmetrical=True)
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
        help_text="Select what type of content to display as the project cover."
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
    

class Certificate(models.Model):
    """
    Represents a certificate or achievement.
    Includes icon, title, subtitle, description, date, and optional URL.
    """
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

    class Meta:
        ordering = ['-date'] # Automatically order by date descending
        verbose_name = "Certificate / Project"
        verbose_name_plural = "Certificates & Projects"

    def __str__(self):
        return self.title_en or self.title_es or self.title
    
