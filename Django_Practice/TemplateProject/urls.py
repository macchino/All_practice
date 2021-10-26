from django.contrib import admin
from django.urls import path, include

import TemplateApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template_app/', include('TemplateApp.urls')),
]
