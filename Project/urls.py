from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('', include('Products.urls')),
]
