from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    #ツイート本文
    content = models.TextField()
    #ツイートした人 主キー制約 ユーザーが消されたら投稿も消す
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    #ツイート時刻
    date_posted = models.DateTimeField(default = timezone.now)
    #いいね 初期値0
    likes = models.IntegerField(default = 0)

    #管理者画面で見れるようにする(?)
    def __str__(self):
        return self.content