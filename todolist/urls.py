# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, toggle_is_finished,delete_task

app_name = 'todolist' 

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('toggle-is-finished/<int:id>/', toggle_is_finished, name='toggle_is_finished'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]