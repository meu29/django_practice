from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    #views.<<user/views.pyのクラス>>.as_view()
    path("home/", views.HomeView.as_view(), name = "home")
]