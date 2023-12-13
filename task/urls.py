from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.Login,name='login'),
    path('register',views.register_view,name='register'),
    path('single/<id>',views.single_view,name='single_view'),
    path('create',views.add_App,name='create'),
    path('points',views.view_points,name='points'),
    path('profile/<id>',views.view_profile,name='profile'),
    path('tasks',views.view_app_task,name='tasks'),
    path('task/<id>',views.single_task_view,name='task_view')
]
