"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from sub_project import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home_page,name='home_page'),
    path('',TemplateView.as_view(template_name='login.html'),name='login'),
    url(r'^register/$',views.register,name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^form1/$',views.index,name='index'),
    url(r'^forms/$',views.form_view,name='form_view'),
    url(r'^retrieve/$',views.form_rets,name='form_rets'),
    url(r'^Fsearch/$',views.searchview,name='searchview'),
    url(r'^find_search/$',views.find_search,name='find_search'),
    url(r'^sfile/$', views.showfile,name='showfile'),
    ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




    #url(r'^user_login/$',views.login_page,name='login_page'),

    #url(r'^register/$',views.register,name='register'),

    #url(r'^form/$',views.form_log,name='form_log'),



    #url(r'^$',views.form_dis,name='form_dis')
    #url(r'^home/$',views.home_page,name='home')
    #url(r'^login/$', auth_views.login),
