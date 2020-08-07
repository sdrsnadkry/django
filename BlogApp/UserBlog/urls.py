from django.urls import path
from .views import HomePage, Register, Login, Activate, ListBlog, Logout, CreateBlog, BlogDetails, BlogUpdate, \
    BlogDelete, ProfileUpdate, BlogDetailsPage

urlpatterns = [
    path('', HomePage.as_view(), name='Homepage'),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),

    path('register/', Register.as_view(), name='Register'),
    path('activate/<uid>/', Activate.as_view(), name='activate'),

    path('profile/', ListBlog.as_view(), name='Profile'),
    # path('profile-update/<int:pk>/', ProfileUpdate.as_view(), name='profile-update'),
    path('profile-update/', ProfileUpdate.as_view(), name='profile-update'),

    path('create-blog/', CreateBlog.as_view(), name='create-blog'),
    path('blog-detail/<int:pk>/', BlogDetails.as_view(), name='blog-detail'),
    path('blog-update/<int:pk>/', BlogUpdate.as_view(), name='update-blog'),
    path('blog-delete/<int:pk>/', BlogDelete.as_view(), name='delete-blog'),

    path('blog-detail-page/<int:pk>/', BlogDetailsPage.as_view(), name='blog-detail-page'),

]
