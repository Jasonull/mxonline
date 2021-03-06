"""mxonline URL Configuration

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
from django.urls import re_path, include
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdViewGet, ResetPwdViewPost
from organization.views import OrgView
from mxonline import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^xadmin/', xadmin.site.urls),
    re_path('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    re_path('^login/', LoginView.as_view(), name="login"),
    re_path('^register/', RegisterView.as_view(), name="register"),
    re_path(r'^captcha/', include('captcha.urls')),
    re_path(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    re_path(r'^forget_pwd/$', ForgetPwdView.as_view(), name="forget_pwd"),
    re_path(r'^reset_pwd_get/(?P<reset_code>.*)/$', ResetPwdViewGet.as_view(), name="reset_pwd_get"),
    re_path(r'^reset_pwd_post/$', ResetPwdViewPost.as_view(), name="reset_pwd_post"),
    re_path(r'^org_list/$', OrgView.as_view(), name="org_list"),
    #配置上传文件的访问处理
    re_path(r'^media/(?P<path>.*)/$', serve, {"document_root": settings.MEDIA_ROOT}),
]
