from django.views.generic import ListView
#tweet/models.pyのPostクラスをインポート?
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = "posts"
    #表示する順番 -で新しい投稿から表示?
    ordering = ["-date_posted"]
    #1ページに表示するツイート数
    paginate_by = 5