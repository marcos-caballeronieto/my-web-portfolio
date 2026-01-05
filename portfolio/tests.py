from django.test import TestCase
from django.urls import reverse
from .models import Category, Project, Certificate

# Create your tests here.

class CategoryModelTest(TestCase):
    """
    Test cases for the Category model.
    """
    def test_category_creation(self):
        """
        Test that a Category can be created and its string representation is correct.
        """
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")

    def test_category_unique_name(self):
        """
        Test that category names must be unique.
        """
        Category.objects.create(name="Unique Category")
        with self.assertRaises(Exception):
            Category.objects.create(name="Unique Category")

class ProjectModelTest(TestCase):
    """
    Test cases for the Project model.
    """
    def setUp(self):
        """
        Set up test data for Project tests.
        """
        self.category = Category.objects.create(name="Test Category")

    def test_project_creation(self):
        """
        Test that a Project can be created and its string representation is correct.
        """
        project = Project.objects.create(
            title="Test Project",
            description="Test description",
            relevance=3
        )
        project.categories.add(self.category)
        self.assertEqual(str(project), "Test Project")

    def test_project_relevance_choices(self):
        """
        Test that relevance field accepts valid choices.
        """
        project = Project.objects.create(
            title="Test Project",
            description="Test description",
            relevance=Project.Relevance.HIGH
        )
        self.assertEqual(project.relevance, 4)

class CertificateModelTest(TestCase):
    """
    Test cases for the Certificate model.
    """
    def test_certificate_creation(self):
        """
        Test that a Certificate can be created and its string representation is correct.
        """
        certificate = Certificate.objects.create(
            title="Test Certificate",
            subtitle="Test Subtitle",
            description="Test description",
            date="2023-01-01"
        )
        self.assertEqual(str(certificate), "Test Certificate")

class ViewTests(TestCase):
    """
    Test cases for views.
    """
    def setUp(self):
        """
        Set up test data for view tests.
        """
        self.category = Category.objects.create(name="Test Category")
        self.project = Project.objects.create(
            title="Test Project",
            description="Test description",
            relevance=3
        )
        self.project.categories.add(self.category)
        self.certificate = Certificate.objects.create(
            title="Test Certificate",
            subtitle="Test Subtitle",
            description="Test description",
            date="2023-01-01"
        )

    def test_home_view(self):
        """
        Test that the home view returns a 200 status and contains expected context.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('featured_projects', response.context)
        self.assertIn('latest_projects', response.context)
        self.assertIn('certificates', response.context)

    def test_project_detail_view(self):
        """
        Test that the project detail view returns a 200 status for existing project.
        """
        response = self.client.get(reverse('project_detail', args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project'], self.project)

    def test_project_list_view(self):
        """
        Test that the project list view returns a 200 status and contains projects.
        """
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('projects', response.context)
        self.assertIn('categories', response.context)

    def test_about_view(self):
        """
        Test that the about view returns a 200 status.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('certificates', response.context)
