from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_files.urls')),
    path('staff/', include('django.contrib.auth.urls')),
    path('', include('staff.urls')),
]
