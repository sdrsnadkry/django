from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from .models import UserDetail, UserEducation, Task, Popup
from django.forms import ValidationError
from tempus_dominus.widgets import DateTimePicker


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['designation', 'address', 'city', 'country', 'code', 'mobile', 'bio']
        widgets = {
            'designation': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class UserEducationForm(forms.ModelForm):
    pass


class TaskForm(forms.ModelForm):
    CHOICES = [('High', 'High '),
               ('Medium', 'Medium'),
               ('Low', 'Low')]
    priority = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'owner': forms.Select(attrs={
                'class': 'form-control',
            }),
            'assignee': forms.Select(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'end_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'reminder_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),

        }


class PopupForm(forms.ModelForm):
    CHOICES = [('Urgent', 'Urgent '),
               ('Reminder', 'Reminder'),
               ('Notice', 'Notice')]
    priority = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Popup
        fields = ['priority', 'title', 'description', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'end_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }
