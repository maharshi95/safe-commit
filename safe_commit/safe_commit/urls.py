"""safe_commit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from app_server.views import app_views as app_server_views
from app_server.views.viewsets import ProjectListCreateAPIView, RetrieveProjectAPIView, ProjectJobListCreateView, ProjectJobRetrieveAPIView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/1.0/docs/', get_swagger_view(title='Safe Commit API')),

    url(r'^api/1.0/', include(router.urls)),
    url(r'^api/1.0/health', view=app_server_views.health_api),

    url(r'^api/1.0/projects', view=ProjectListCreateAPIView.as_view()),
    url(r'^api/1.0/projects/(?P<id>[\w-]+)/$', view=RetrieveProjectAPIView.as_view()),

    url(r'^api/1.0/project_jobs', view=ProjectJobListCreateView.as_view()),
    url(r'^api/1.0/project_jobs/(?P<id>[\w-]+)/$', view=ProjectJobRetrieveAPIView.as_view()),
]
