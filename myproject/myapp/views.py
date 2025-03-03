from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MyApp

# Create your views here.
def Home(request):
    ItsApp = MyApp.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'ItsApp': ItsApp,
    }

    return HttpResponse(template.render(context, request))