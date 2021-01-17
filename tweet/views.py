#ファイル名にビューとあるが実際はコントローラーの役割?
from django.http import HttpResponse
import json
from django.shortcuts import render
#tweet/models.pyのPostクラスをインポート?
from .models import Post

#@ensure_csrf_cookie

def indexView(request):
    #model = Post
    return render(request, "tweet/index.html")

def aboutView(request):
    return render(request, "tweet/about.html")

#https://hitsujicloud.com/2020/03/09/post-346/
def fetch(request):
    if request.method == "GET":
        #QuerySetをjsonに変換  json.dumps()だとダメ
        tweets = list(Post.objects.all().values()) 
        for i in range(len(tweets)):
            tweets[i]["date_posted"] = str(tweets[i]["date_posted"])
        response = json.dumps({"tweets": json.dumps(tweets)})
    else:
        request = json.loads(request.body.decode())
        print(request["content"])
        #posted_dateとlikesは省略(自動で追加してくれる)
        #newPost = Post(content = "かかか", author = "bot")
        #newPost.save()
        response = json.dumps({"message": "まんちお！"}) 

    return HttpResponse(response) 
        
