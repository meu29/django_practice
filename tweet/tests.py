from django.test import TestCase
from .models import Post

class PostTestCace(TestCase):
 
    #メソッド名をtestから始めないと実行されない
    def test_post_tweet(self):
        content = "これはテストです"
        Post(content = content, author = "test_bot").save()
        newTweet = Post.objects.filter(content__contains = content).values()[0]
        return self.assertEqual(content, newTweet["content"])


