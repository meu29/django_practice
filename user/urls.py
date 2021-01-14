from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    #http://127.0.0.1:8000/home にリクエストが来たときの処理
    #views.<<user/views.pyのクラス>>.as_view()
    path("home/", views.HomeView.as_view(), name = "home")
]