from django.shortcuts import render
from .models import Project

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})
