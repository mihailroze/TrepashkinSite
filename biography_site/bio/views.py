from django.shortcuts import render
from .models import Biography

def bio_home(request):
    bio = Biography.objects.first()  # Берем первую запись
    return render(request, 'bio/bio_home.html', {'bio': bio})