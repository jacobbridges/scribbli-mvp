"""scribbli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from rest_framework.routers import SimpleRouter


# =============================================================================
# API URLs

from scribbli.universe.apiviews import (
    LocationViewSet,
)

router = SimpleRouter()
router.register('location', LocationViewSet, basename='location')


# =============================================================================
# Application URLs

urlpatterns = [
    path('__graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('profiles/', include('scribbli.profiles.urls')),
    path('characters/', include('scribbli.characters.urls')),
    path('stories/', include('scribbli.stories.urls')),
    path('', include('scribbli.universe.urls')),
]
