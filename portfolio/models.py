from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='projects')
    class relvance(models.IntegerChoices):
        VERY_LOW = 1, 'Very Low'
        LOW = 2, 'Low'
        MEDIUM = 3, 'Medium'
        HIGH = 4, 'High'
        VERY_HIGH = 5, 'Very High'
    relevance = models.IntegerField(choices=relvance.choices, default=relvance.MEDIUM)

    def __str__(self):
        return self.title
    
