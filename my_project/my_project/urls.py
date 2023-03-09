from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('cars/', include('cars_db.urls')),
    path('cars/details/<int:id>', include('cars_db.urls')),
    path('admin/', admin.site.urls),
]
