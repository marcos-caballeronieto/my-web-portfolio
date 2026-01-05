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
    short_description = models.TextField(default='No description', blank=True)
    description = CKEditor5Field('Description', config_name='default')
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='projects')
    class Relevance(models.IntegerChoices):
        VERY_LOW = 1, 'Very Low'
        LOW = 2, 'Low'
        MEDIUM = 3, 'Medium'
        HIGH = 4, 'High'
        VERY_HIGH = 5, 'Very High'
    relevance = models.IntegerField(choices=Relevance.choices, default=Relevance.MEDIUM)

    def __str__(self):
        return self.title
    

class Certificate(models.Model):
    """
    Represents a certificate or achievement.
    Includes icon, title, subtitle, description, date, and optional URL.
    """
    icon = models.CharField(max_length=10, default='📜', verbose_name="Icon/Emoji")
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle / Organization")
    description = models.TextField(verbose_name="Description")
    date = models.DateField(verbose_name="Date Obtained")
    url = models.URLField(blank=True, null=True, verbose_name="Link (Optional)")

    class Meta:
        ordering = ['-date'] # Automatically order by date descending
        verbose_name = "Certificate / Project"
        verbose_name_plural = "Certificates & Projects"

    def __str__(self):
        return self.title
    
