from django.contrib import admin
from django.urls import path
from django.conf import settings
from main.views import home
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
