from django.shortcuts import render, get_object_or_404
from .models import Project, Category, Certificate

# Create your views here.

def home(request):
    """
    Renders the home page displaying featured projects, latest projects, and certificates.

    Retrieves featured projects, non-featured projects ordered by ID descending,
    and all certificates. Passes them to the home.html template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home.html template with context data.
    """
    featured_projects = Project.objects.filter(is_featured=True)
    latest_projects = Project.objects.filter(is_featured=False).order_by('-pk')
    certificates = Certificate.objects.all()
    context = {
        'featured_projects': featured_projects,
        'latest_projects': latest_projects,
        'certificates': certificates,
    }
    return render(request, './home.html', context)

def about(request):
    """
    Renders the about page with language selection and certificates.

    Retrieves the language from query parameters (default 'en') and all certificates.
    Passes them to the about.html template.

    Args:
        request: The HTTP request object, may include 'lang' query parameter.

    Returns:
        HttpResponse: Rendered about.html template with context data.
    """
    language = request.GET.get('lang', 'en')
    certificates = Certificate.objects.all()
    context = {
        'language': language,
        'certificates': certificates,
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