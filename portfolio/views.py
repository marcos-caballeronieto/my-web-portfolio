from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from .models import (
    Project,
    Category,
    Certificate,
    CertificateCategory,
    SkillCategory,
    Skill,
)

# Create your views here.

def home(request):
    """
    Renders the home page displaying featured projects, latest projects, and certificates.

    Retrieves featured projects, non-featured projects ordered by ID descending,
    and visible certificates. Passes them to the home.html template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home.html template with context data.
    """
    featured_projects = Project.objects.filter(is_featured=True)
    latest_projects = Project.objects.filter(is_featured=False).order_by('-pk')
    certificates = Certificate.objects.filter(is_visible=True)
    context = {
        'featured_projects': featured_projects,
        'latest_projects': latest_projects,
        'certificates': certificates,
    }
    return render(request, './home.html', context)

def about(request):
    """
    Renders the about page with language selection, certificates, and skills.

    Retrieves the language from query parameters (default 'en'), visible certificates
    marked for the About page, and visible skill categories with their About skills.
    Passes them to the about.html template.

    Args:
        request: The HTTP request object, may include 'lang' query parameter.

    Returns:
        HttpResponse: Rendered about.html template with context data.
    """
    language = request.GET.get('lang', 'en')
    certificates = Certificate.objects.filter(is_visible=True, show_on_about=True).prefetch_related('categories')
    about_skills_prefetch = Prefetch(
        'skills',
        queryset=Skill.objects.filter(is_visible=True, show_on_about=True),
    )
    skill_categories = (
        SkillCategory.objects.filter(
            is_visible=True,
            skills__is_visible=True,
            skills__show_on_about=True,
        )
        .distinct()
        .prefetch_related(about_skills_prefetch)
    )
    context = {
        'language': language,
        'certificates': certificates,
        'skill_categories': skill_categories,
    }
    return render(request, './about.html', context)

def project_detail(request, slug):
    """
    Renders the detail page for a specific project.

    Retrieves the project by slug or returns 404 if not found.
    Also retrieves related projects to display them at the bottom.
    Passes the project and related_projects to the project_detail.html template.

    Args:
        request: The HTTP request object.
        slug (str): The slug of the project.

    Returns:
        HttpResponse: Rendered project_detail.html template with project data.
    """
    project = get_object_or_404(Project, slug=slug)
    related_projects = project.related_projects.all()
    return render(request, './project_detail.html', {
        'project': project,
        'related_projects': related_projects
    })

def project_list(request):
    """
    Renders the project list page, optionally filtered by category.

    If a category is specified in query parameters, filters projects by that category
    and orders by relevance descending. Otherwise, shows all projects ordered by relevance.
    Retrieves all categories for navigation.

    Args:
        request: The HTTP request object, may include 'category' query parameter.

    Returns:
        HttpResponse: Rendered project_list.html template with projects and categories.
    """
    category_name = request.GET.get('category')
    base_query = Project.objects.filter(is_miniproject=False)
    
    if category_name:
        projects = base_query.filter(categories__name=category_name).order_by('-relevance')
    else:
        projects = base_query.order_by('-relevance')
    
    main_categories = Category.objects.filter(is_main=True)
    other_categories = Category.objects.filter(is_main=False)
    
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'other_categories': other_categories,
        'active_category': category_name,
    }
    return render(request, './project_list.html', context)

def mini_projects_list(request):
    """
    Renders the miniprojects list page, optionally filtered by category.
    """
    category_name = request.GET.get('category')
    base_query = Project.objects.filter(is_miniproject=True)
    
    if category_name:
        projects = base_query.filter(categories__name=category_name).order_by('-relevance')
    else:
        projects = base_query.order_by('-relevance')
    
    main_categories = Category.objects.filter(projects__is_miniproject=True, is_main=True).distinct()
    other_categories = Category.objects.filter(projects__is_miniproject=True, is_main=False).distinct()
    
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'other_categories': other_categories,
        'active_category': category_name,
    }
    return render(request, './mini_projects_list.html', context)


def certificates_list(request):
    """
    Renders the dedicated certificates and courses page with type and category filtering.
    """
    category_name = request.GET.get('category')
    item_type = request.GET.get('type')
    language = request.GET.get('lang', 'en')

    certificates = Certificate.objects.filter(is_visible=True).prefetch_related('categories')

    if item_type in (Certificate.ItemType.CERTIFICATE, Certificate.ItemType.COURSE):
        certificates = certificates.filter(item_type=item_type)
    else:
        item_type = None

    if category_name:
        certificates = certificates.filter(categories__name=category_name).distinct()

    main_categories = CertificateCategory.objects.filter(is_main=True)
    other_categories = CertificateCategory.objects.filter(is_main=False)

    context = {
        'certificates': certificates,
        'main_categories': main_categories,
        'other_categories': other_categories,
        'active_category': category_name,
        'active_type': item_type,
        'language': language,
    }
    return render(request, './certificates_list.html', context)


def skills_list(request):
    """
    Renders the dedicated technical skills page organized and filterable by category.
    """
    category_name = request.GET.get('category')
    language = request.GET.get('lang', 'en')

    visible_skills_prefetch = Prefetch(
        'skills',
        queryset=Skill.objects.filter(is_visible=True),
    )
    skill_categories = SkillCategory.objects.filter(is_visible=True).prefetch_related(visible_skills_prefetch)

    if category_name:
        skill_categories = skill_categories.filter(name=category_name)

    main_categories = SkillCategory.objects.filter(is_visible=True, is_main=True)
    other_categories = SkillCategory.objects.filter(is_visible=True, is_main=False)

    context = {
        'skill_categories': skill_categories,
        'main_categories': main_categories,
        'other_categories': other_categories,
        'active_category': category_name,
        'language': language,
    }
    return render(request, './skills_list.html', context)