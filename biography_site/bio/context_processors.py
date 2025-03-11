from .models import Biography

def bio_context(request):
    bio = Biography.objects.first()
    return {'bio': bio}