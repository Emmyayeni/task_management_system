"""
URL configuration for DE project.

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
from task.views import home,logout_view,staff_home
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('staff_home',staff_home,name='staff_home'),

     # password reset links
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="task/account/password_change_done.html"),name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="task/account/password_change.html"),name='password_change'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name="task/account/password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='task/account/set_password.html'),name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='task/account/reset_password.html'),name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="task/account/password_reset_complete.html"),name='password_reset_complete'),
    path('api/v1/',include('task.api.urls')),
    path('',include('task.urls')),
    path('logout',logout_view,name='logout')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

