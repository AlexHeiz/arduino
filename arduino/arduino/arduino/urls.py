from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', include('test_timer.urls')),
    path('api/', include('api.urls')),
]
