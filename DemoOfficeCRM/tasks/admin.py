from django.contrib import admin
from .models import UserEducation,UserDetail, Task, TasksStatus, Popup

# Register your models here.

admin.site.register([UserEducation, UserDetail, Task, TasksStatus, Popup])
