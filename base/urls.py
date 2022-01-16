from django import urls
# from django.conf.urls import urls
from django.urls import path, include
from .views import TaskDelete, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView,TaskLogin,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TaskLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name= 'task'),
    path('task-create/', TaskCreate.as_view(), name='task_create' ),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name= 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name= 'task-delete'),
    
]