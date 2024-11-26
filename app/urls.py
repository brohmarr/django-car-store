from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import home, cars_view, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cars/', cars_view, name='cars_list'),
    path('about/', about, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
