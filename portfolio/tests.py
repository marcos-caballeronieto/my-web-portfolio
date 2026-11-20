from django.test import TestCase
from django.urls import reverse
from .models import (
    Category,
    Project,
    Certificate,
    CertificateCategory,
    SkillCategory,
    Skill,
)

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

    def test_project_validation_image_required(self):
        """
        Test that ValidationError is raised if cover_type is IMAGE and no image is provided.
        """
        from django.core.exceptions import ValidationError
        project = Project(
            title="Test Project No Image",
            description="Test description",
            cover_type=Project.CoverType.IMAGE
        )
        with self.assertRaises(ValidationError):
            project.full_clean()

    def test_project_validation_image_optional_for_threejs(self):
        """
        Test that validation passes without an image if cover_type is THREEJS.
        """
        project = Project(
            title="Test Project ThreeJS",
            description="Test description",
            cover_type=Project.CoverType.THREEJS,
            list_cover_type=Project.CoverType.THREEJS
        )
        # Should not raise validation error
        project.full_clean()

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

class CertificateCategoryModelTest(TestCase):
    """
    Test cases for the CertificateCategory model.
    """
    def test_certificate_category_creation_and_str(self):
        cat = CertificateCategory.objects.create(
            name="AI & ML",
            name_en="AI & Machine Learning",
            name_es="IA y Machine Learning",
        )
        self.assertEqual(str(cat), "AI & Machine Learning")


class SkillModelsTest(TestCase):
    """
    Test cases for SkillCategory and Skill models.
    """
    def test_skill_category_and_skill_creation(self):
        cat = SkillCategory.objects.create(
            name="Testing Category",
            name_en="Testing Category EN",
            name_es="Categoría de Prueba",
            icon="fas fa-vial",
            order=10,
        )
        skill = Skill.objects.create(
            name="Pytest",
            name_en="Pytest EN",
            name_es="Pytest ES",
            category=cat,
            order=1,
        )
        self.assertEqual(str(cat), "Testing Category EN")
        self.assertEqual(str(skill), "Pytest EN")
        self.assertIn(skill, cat.skills.all())


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
            slug="test-project",
            description="Test description",
            relevance=3
        )
        self.project.categories.add(self.category)
        self.cert_category = CertificateCategory.objects.create(
            name="Artificial Intelligence",
            name_en="Artificial Intelligence",
            name_es="Inteligencia Artificial",
            is_main=True,
        )
        self.other_cert_category = CertificateCategory.objects.create(
            name="Cloud",
            name_en="Cloud",
            name_es="Nube",
            is_main=False,
        )
        self.certificate = Certificate.objects.create(
            item_type=Certificate.ItemType.CERTIFICATE,
            title="Test Certificate",
            subtitle="Test Subtitle",
            description="Test description",
            date="2023-01-01",
            is_visible=True,
            show_on_about=True,
        )
        self.certificate.categories.add(self.cert_category)
        self.course = Certificate.objects.create(
            item_type=Certificate.ItemType.COURSE,
            title="Test Course",
            subtitle="Course Org",
            description="Course description",
            date="2024-02-01",
            is_visible=True,
            show_on_about=False,
        )
        self.course.categories.add(self.other_cert_category)
        self.hidden_certificate = Certificate.objects.create(
            item_type=Certificate.ItemType.CERTIFICATE,
            title="Hidden Certificate",
            subtitle="Hidden Org",
            description="Hidden description",
            date="2024-03-01",
            is_visible=False,
            show_on_about=True,
        )

        self.skill_category = SkillCategory.objects.create(
            name="Test Skills",
            name_en="Test Skills",
            name_es="Habilidades de Prueba",
            is_main=True,
            is_visible=True,
            order=10,
        )
        self.hidden_skill_category = SkillCategory.objects.create(
            name="Hidden Skill Category",
            is_main=False,
            is_visible=False,
            order=20,
        )
        self.skills_page_only_category = SkillCategory.objects.create(
            name="Skills Page Only Category",
            is_main=False,
            is_visible=True,
            show_on_about=False,
            order=25,
        )
        self.skills_page_only_cat_skill = Skill.objects.create(
            name="Skill In Non-About Category",
            category=self.skills_page_only_category,
            is_visible=True,
            show_on_about=True,
        )
        self.about_skill = Skill.objects.create(
            name="Visible About Skill",
            category=self.skill_category,
            is_visible=True,
            show_on_about=True,
        )
        self.non_about_skill = Skill.objects.create(
            name="Skills Page Only",
            category=self.skill_category,
            is_visible=True,
            show_on_about=False,
        )
        self.hidden_skill = Skill.objects.create(
            name="Hidden Skill",
            category=self.skill_category,
            is_visible=False,
            show_on_about=True,
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
        self.assertNotIn(self.hidden_certificate, response.context['certificates'])

    def test_project_detail_view(self):
        """
        Test that the project detail view returns a 200 status for existing project.
        """
        response = self.client.get(reverse('project_detail', args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project'], self.project)

    def test_project_list_view(self):
        """
        Test that the project list view returns a 200 status and contains projects.
        """
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('projects', response.context)
        self.assertIn('main_categories', response.context)
        self.assertIn('other_categories', response.context)

    def test_about_view(self):
        """
        Test that the about view returns a 200 status and filters certificates/skills for About Me.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('certificates', response.context)
        self.assertIn('skill_categories', response.context)
        self.assertIn(self.certificate, response.context['certificates'])
        self.assertNotIn(self.course, response.context['certificates'])
        self.assertNotIn(self.hidden_certificate, response.context['certificates'])

        self.assertNotIn(self.skills_page_only_category, response.context['skill_categories'])
        cat = next(c for c in response.context['skill_categories'] if c == self.skill_category)
        about_skills = list(cat.skills.all())
        self.assertIn(self.about_skill, about_skills)
        self.assertNotIn(self.non_about_skill, about_skills)
        self.assertNotIn(self.hidden_skill, about_skills)

    def test_certificates_list_view(self):
        """
        Test certificates_list view returns 200 and supports category, type, and visibility filtering.
        """
        response = self.client.get(reverse('certificates_list'))
        self.assertEqual(response.status_code, 200)
        certs = list(response.context['certificates'])
        self.assertIn(self.certificate, certs)
        self.assertIn(self.course, certs)
        self.assertNotIn(self.hidden_certificate, certs)

        # Filter by item_type=COURSE
        response_course = self.client.get(reverse('certificates_list'), {'type': 'COURSE'})
        self.assertEqual(response_course.status_code, 200)
        course_certs = list(response_course.context['certificates'])
        self.assertIn(self.course, course_certs)
        self.assertNotIn(self.certificate, course_certs)

        # Filter by category
        response_cat = self.client.get(reverse('certificates_list'), {'category': 'Artificial Intelligence'})
        self.assertEqual(response_cat.status_code, 200)
        cat_certs = list(response_cat.context['certificates'])
        self.assertIn(self.certificate, cat_certs)
        self.assertNotIn(self.course, cat_certs)

    def test_skills_list_view(self):
        """
        Test skills_list view returns 200 and filters by category and visibility.
        """
        response = self.client.get(reverse('skills_list'))
        self.assertEqual(response.status_code, 200)
        cats = list(response.context['skill_categories'])
        self.assertIn(self.skill_category, cats)
        self.assertNotIn(self.hidden_skill_category, cats)

        cat = next(c for c in cats if c == self.skill_category)
        visible_skills = list(cat.skills.all())
        self.assertIn(self.about_skill, visible_skills)
        self.assertIn(self.non_about_skill, visible_skills)
        self.assertNotIn(self.hidden_skill, visible_skills)

        # Filter by category
        response_cat = self.client.get(reverse('skills_list'), {'category': 'Test Skills'})
        self.assertEqual(response_cat.status_code, 200)
        self.assertEqual(list(response_cat.context['skill_categories']), [self.skill_category])
