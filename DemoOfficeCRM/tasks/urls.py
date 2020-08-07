from django.urls import path
from .views import task_base, list_users, delete_user, handle_login, handle_logout, update_user_details, tasks_view, \
    delete_task, your_task, popup

# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', handle_login, name='login'),
    path('logout/', handle_logout, name='logout'),
    path('dashboard/', task_base, name="dashboard"),


    path('list-users/', list_users, name="users"),
    # path('delete-user/', delete_user)
    path('list-users/delete-user/<int:id>/', delete_user),
    path('update-user-details/', update_user_details, name='updateuser'),


    path('tasks/', tasks_view, name='tasks'),
    # path('pagination/', pagination, name='pagination'),
    path('tasks/delete-task/<int:id>/', delete_task),
    path('your-task/', your_task, name='yourtask'),


    path('popup/', popup, name='popup'),

]
