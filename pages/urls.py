from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="root"),
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about" ),
    path("contact/", views.contact_view, name="contact"),
    path('website/', views.website_view, name="website"),
    path('template/', views.template_view, name="template"),
    path('resume/', views.resume_view, name='resume'),
    ]