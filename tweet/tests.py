from django.test import TestCase
from .models import Post

class PostTestCace(TestCase):

    content = "これはテストです"

    #メソッド名をtestから始めないと実行されない
    #各メソッドの終了時にテーブルの内容は消える(?)

    def test_post_tweet(self):
        Post(content = PostTestCace.content, author = "test_bot").save()
        newTweet = Post.objects.filter(content__contains = PostTestCace.content).values()[0]
        return self.assertEqual(PostTestCace.content, newTweet["content"])

    def test_update_tweet(self):
        Post(content = PostTestCace.content, author = "test_bot").save()
        newTweet = Post.objects.filter(content__contains = PostTestCace.content).values()[0]
        Post.objects.filter(content__contains = PostTestCace.content).update(likes = 1)
        newTweet = Post.objects.filter(content__contains = PostTestCace.content).values()[0]
        return self.assertEqual(1, newTweet["likes"])
    
    def test_delete_tweet(self):
        Post(content = PostTestCace.content, author = "test_bot").save()
        newTweet = Post.objects.filter(content__contains = PostTestCace.content).values()[0]
        Post.objects.filter(content__contains = PostTestCace.content).delete()
        newTweet = Post.objects.filter(content__contains = PostTestCace.content).values()
        return self.assertEqual(0, len(newTweet))

