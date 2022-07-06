from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("team/", views.team, name="team"),
    path("contact/", views.contact, name="contact"),
    path("home/", views.home, name="home"),



]
