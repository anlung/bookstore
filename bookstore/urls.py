"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from store import views  # ,urls

urlpatterns = [
      url(r'^$', views.index, name='index'),
      # url(r'^store/', views.store, name='store'),
      url(r'^store/', include('store.urls'), name='store'),
      # url(r'^accounts/', include('registration.backends.simple.urls')),
      url(r'^accounts/', include('registration.backends.default.urls')),
      # url('', include('social.apps.django_app.urls', namespace='social')),
      url('', include('social_django.urls', namespace='social')),
      # url(r'^admin/', include(admin.site.urls)),
      url(r'^admin/', admin.site.urls),
]

