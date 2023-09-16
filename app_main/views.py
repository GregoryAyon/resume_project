from django.shortcuts import render, get_object_or_404
from app_main.models import *

# Create your views here.


def index_view(request):
    context = {
        'info': get_object_or_404(InfoModel, id=1),
        'skills': SkillsQualificationsModel.objects.all().order_by('id'),
        'stacks': TechStackModel.objects.all().order_by('id'),
        'edu': EducationsModel.objects.all().order_by('id'),
        'publications': PublicationModel.objects.all().order_by('id'),
        'projects': ProjectsModel.objects.all().order_by('id'),
        'works': WorksModel.objects.all().order_by('id'),
    }

    return render(request, 'app_main/index.html', context)
