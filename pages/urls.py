from django.contrib import admin
from .views import homepageview
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepageview, name= 'home'),
    path('', include('pages.urls')),
]
