from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerialers
# Create your views here.
def drink_list(request):
    drinks=Drink.objects.all()
    serializer=DrinkSerialers(drinks,many=True)
    return JsonResponse(serializer.data,safe=False)
