"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from api.views import (
    ClientListCreateView,
    ClientRetrieveUpdateDestroyView,
    ProjectCreateView,
    UserProjectsView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:id>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('clients/<int:id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]
