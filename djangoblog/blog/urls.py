from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    YearArchiveView,
    )
from django.views.generic.dates import ArchiveIndexView
from .models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('archive/', ArchiveIndexView.as_view(model=Post, date_field="created_at", template_name='blog/archive.html'), name='post-archive'),
    path('archive/<int:year>/', YearArchiveView.as_view(model=Post, date_field="created_at", make_object_list=True, template_name='blog/year_archive.html'), name='post-year-archive'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
