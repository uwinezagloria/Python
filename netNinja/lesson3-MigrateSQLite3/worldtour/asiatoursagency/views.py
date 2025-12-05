from django.shortcuts import render
from .models import Tour
# Create your views here.
def index(request):
    tours=Tour.objects.all() #fetching all object of Tour in database model
    context={'tours':tours} #creating dictionary that has all tours
    return render(request,"tours/index.html",context)
