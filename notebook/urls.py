from django.urls import path
from notebook import views

urlpatterns = [
    path("",views.notebook,name="notebook"),
    path("home",views.home,name="home"),
    path("home1",views.home1,name="home1"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
]
