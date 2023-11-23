from django.contrib import admin
from django.urls import path, include
from copywriting import views
from settings.views import update_profile


urlpatterns = [
    path('copywriting/', include('copywriting.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile', update_profile, name='profile'),
]
