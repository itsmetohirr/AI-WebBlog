from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('generate-blog/', views.generate_blog, name='generate-blog'),
    path('blog-list/', views.blog_list, name='blog-list'),
]
