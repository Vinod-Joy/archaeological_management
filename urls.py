"""adb URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . import views

admin.autodiscover()
app_name='home'

urlpatterns = [
    url(r'^home/',views.home),
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^arch/', include('arch.urls')),
    url(r'^$',views.hello),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', auth_view.logout, {'template_name': 'logged_out.html'}, name='logout'),


]
handler404 = 'views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
