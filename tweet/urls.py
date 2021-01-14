from django.urls import path
from . import views

app_name = "tweet"

urlpatterns = [
    #http://127.0.0.1:8000 にリクエストが来たらビューを返す
    #第一引数がhogeならhttp://127.0.0.1:8000/hogeにリクエストが来た時
    #tweet/views.pyのPostListViewクラス
    path("", views.PostListView.as_view(), name="index")
]
