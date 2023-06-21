from django.shortcuts import render
from store.models import Hospital
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'includes/aboutus.html')