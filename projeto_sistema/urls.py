from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('app_cadastro.urls'), name='app_cadastro_urls'),
]
