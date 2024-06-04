from django.shortcuts import render
from .models import addAuto
# Create your views here.
def index(req):
    return render(req, 'index.html', context={'auto': addAuto.objects.all()})