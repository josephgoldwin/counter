from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Counter

def home(request):
    counter = Counter.objects.first()
    return render(request, "counter.html", {"value": counter.value})

def increment(request):
    counter = Counter.objects.first()
    counter.value += 1
    counter.save()
    return JsonResponse({"value": counter.value})
