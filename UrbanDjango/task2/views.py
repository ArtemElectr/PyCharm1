from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def func_temp(request):
    return render(request, 'func_template.html')


class ClTemplate(TemplateView):
    template_name = 'class_template.html'


