from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'profile/', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project/(?P<project_id>[0-9])$',views.project,name ='project'),
    url(r'^post/', views.upload_form, name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)