from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cooking_base_app/', include('cooking_base_app.urls')),
    path('admin/', admin.site.urls),
]
