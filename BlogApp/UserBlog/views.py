from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View, TemplateView, ListView, CreateView, FormView, DetailView, UpdateView, DeleteView
from rest_framework.generics import get_object_or_404

from .models import Blog

from .forms import RegisterForm, LoginForm, BlogForm, UserUpdateForm

User = get_user_model()


# Create your views here.

class HomePage(ListView):
    template_name = 'home.html'
    queryset = Blog.objects.all()
    context_object_name = 'blog_list'
    paginate_by = 3


class Activate(View):
    def get(self,request, uid):
        uids = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(email=uids)

        if user is not None:
            user.is_active = True
            user.save()

            messages.success(self.request, "User Activated Successfully. Proceed To Login")
            return redirect('/login')
        else:
            messages.error(self.request, "Invalid Activation Link")
            return redirect('/login')


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = '/login'

    def form_valid(self, form):
        # print(form.cleaned_data)
        model = form.save(commit=False)
        model.is_active = False
        model.password = make_password(form.cleaned_data['password'])
        model.save()

        current_site = get_current_site(self.request)

        subject = 'Email Verification for Blog page'
        from_email = 'admin@admin.com'
        recipient = form.cleaned_data['email']

        message = render_to_string('user/activate.html', {
            'user': form.cleaned_data['first_name'],
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(form.cleaned_data['email']))

        })
        send_mail(subject, message, from_email, [recipient])

        messages.success(self.request, 'Account Created Successfully, Check Your Email For Verifications !!')

        return super().form_valid(form)


class Login(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/profile'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(username=email, password=password, is_active=True)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Logged In Successfully")
        else:
            messages.error(self.request, "Invalid Credentials")
            return redirect('/login')

        return super().form_valid(form)


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        try:
            logout(request)
            messages.success(self.request, 'Logged Out Successfully')
            return redirect('/login')
        except:
            messages.error(self.request, 'Could Not Logout')
            return redirect('/profile')


class ListBlog(LoginRequiredMixin, ListView):
    template_name = 'blog/blog-list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Blog.objects.filter(author=self.request.user)
        else:
            queryset = Blog.objects.none()

        return queryset


class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'blog/blog-create.html'
    success_url = '/profile'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.author = self.request.user
        model.save()
        messages.success(self.request, "BLog Created Successfully")
        return super().form_valid(form)


class BlogDetails(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/blog-detail.html'
    context_object_name = 'blog'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id, author=self.request.user)


class BlogUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog-update.html'
    form_class = BlogForm
    success_url = '/profile'
    success_message = 'BLog Updated Successfully'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id, author=self.request.user)


class BlogDelete(DeleteView):
    model = Blog
    success_url = '/profile'
    success_message = 'BLog Deleted Successfully'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id, author=self.request.user)


class ProfileUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/profile-update.html'
    success_url = '/profile'

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)

    def form_valid(self, form):
        model = form.save(commit=False)
        model.password = make_password(form.cleaned_data['password'])
        model.save()
        messages.success(self.request, "Profile Updated Successfully")

        return super().form_valid(form)


class BlogDetailsPage(DetailView):
    template_name = 'blog/blog-details-page.html'
    context_object_name = 'blog'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id)
