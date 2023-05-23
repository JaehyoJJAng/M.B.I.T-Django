from django.shortcuts import render
from .models import Question,Developer,Choice

# Create your views here.

def index(request):
    developers = Developer.objects.all()
    
    context = {
        "developers": developers,
    }
    return render(request=request,template_name='index.html',context=context)