from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views # Add this line to the imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Add this line to the urlpatterns list
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Add this line to the urlpatterns list

