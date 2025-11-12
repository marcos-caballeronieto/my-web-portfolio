from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.order_by('-pk')[:3]
    return render(request, './home.html',{'projects': projects})

def about(request):
    return render(request, './about.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, './project_detail.html', {'project': project})

def project_list(request):
    projects = Project.objects.all()
    return render(request, './project_list.html', {'projects': projects})