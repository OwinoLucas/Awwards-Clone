"""awwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clone import views as clone_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('clone.urls')),
    url(r'register/',clone_views.register, name='register'), 
    url(r'login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    url(r'logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'), 
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^api-token-auth/', obtain_auth_token)
    
]
