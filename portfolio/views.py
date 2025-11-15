from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    latest_projects = Project.objects.filter(is_featured=False).order_by('-pk')
    context = {
        'featured_projects': featured_projects,
        'latest_projects': latest_projects,
    }
    return render(request, './home.html', context)

def about(request):
    return render(request, './about.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, './project_detail.html', {'project': project})

def project_list(request):
    projects = Project.objects.all()
    return render(request, './project_list.html', {'projects': projects})