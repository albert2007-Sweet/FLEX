"""mysite URL Configuration

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
from mysite.views import Indexview, UserCreateView, UserCreateDoneTV, aboutView
from bookmark.views import BookMarkLV
from bookmark.views import BookMarkDV
from bookmark.views import BookMarkCV
from bookmark.views import BookMarkUV
from bookmark.views import BookMarkRV
from blog.views import PostCV, PostUV, PostRV
from blog.views import PostLV, PostDV


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Indexview.as_view(), name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name="register_done"),
    url(r'^bookmark/$', BookMarkLV.as_view(), name='bookmark_index'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookMarkDV.as_view(),name='detail'),
    url(r'^bookmark/add/$',BookMarkCV.as_view(),name='bookmark_create'),
    url(r'^blog/$', PostLV.as_view(), name='blog_index'),
    url(r'^blog/(?P<pk>\d+)/$', PostDV.as_view(), name='blog_detail'),
    url(r'^blog/add/$', PostCV.as_view(), name='blog_create'),
    url(r'^blog/update/(?P<pk>[0-9]+)/$', PostUV.as_view(), name='blog_update'),
    url(r'^blog/delete/(?P<pk>[0-9]+)/$', PostRV.as_view(), name='blog_delete'),
    url(r'^about/$', aboutView.as_view(), name="about"),
    url(r'^bookmark/update/(?P<pk>[0-9]+)/$', BookMarkUV.as_view(), name="bookmark_update"),
    url(r'^bookmark/delete/(?P<pk>[0-9]+)/$', BookMarkRV.as_view(), name="bookmark_delete"),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
