from django.urls import path, include
from . import views

urlpatterns = [
    
    path("",include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]

htmx_urlpatterns = [
    path("check_username/", view=views.check_username, name="check_username"),
]
urlpatterns += htmx_urlpatterns