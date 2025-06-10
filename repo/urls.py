"""
URL configuration for repo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
# from chat.views import get_rooms,send_message
from django.contrib.staticfiles.views import serve

# from file.views import download_document


# def return_static(request, path, insecure=True, **kwargs):
#   return serve(request, path, insecure, **kwargs)
urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    # path('baton/', include('baton.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # 将根URL重定向到/admin/
    # path('get-rooms/', get_rooms, name='get_rooms'),
    # path('chat/send_message/<str:room_name>/', send_message, name='send_message'),
    # path('download/<int:pk>/', download_document, name='download_file'),
    # re_path(r'^static/(?P<path>.*)$', return_static, name='static'),  # 添加这行
#
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if not settings.DEBUG:  # 非DEBUG模式也强制服务静态文件
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
