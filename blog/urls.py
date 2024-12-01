from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.login, name="login"),
    path("blog", views.index, name="index"),
    path("post/<str:slug>", views.detail, name="detail"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("new_url", views.new_url_view, name="new_url"),
    path("contact", views.contact_view, name="contact"),
    path("aboutus", views.aboutus_view, name="about"),
    path("signup", views.signup, name="signup"),
    path('signout', views.signout, name='signout'),
]