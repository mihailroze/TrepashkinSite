from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bio.urls')),
    path('blog/', include('blog.urls')),
]