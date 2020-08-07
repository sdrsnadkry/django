from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, blank=True)
    # active = models.BooleanField(default=True)
    mobile = models.IntegerField(blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=50, blank=True)
    code = models.IntegerField(blank=True)
    bio = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return self.user.username


class UserEducation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    uni = models.CharField(max_length=100, blank=True)
    masters = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Task(TimeStamp):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_owner')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_assignee')
    title = models.CharField(max_length=1000, blank=True)
    description = models.TextField(max_length=10000, blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    reminder_date = models.DateTimeField(blank=True)
    priority = models.CharField(max_length=10, blank=True)
    sent_status = models.BooleanField()

    def __str__(self):
        return self.title


class TasksStatus(TimeStamp):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)
    reassign = models.BooleanField(default=False)
    reassign_description = models.TextField(blank=True)
    reassign_startdate = models.DateTimeField(blank=True)
    reassign_enddate = models.DateTimeField(blank=True)

    def __str__(self):
        return self.task.title


class Popup(TimeStamp):
    priority = models.CharField(max_length=100, default='Urgent')
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Project(TimeStamp):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    assignee = models.ManyToManyField(User, default=69)

    def __str__(self):
        return self.title


