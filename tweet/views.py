#ファイル名にビューとあるが実際はコントローラーの役割?
from django.http import HttpResponse
import json
from django.shortcuts import render
#tweet/models.pyのPostクラスをインポート?
from .models import Post

def indexView(request):
    return render(request, "tweet/index.html")

def aboutView(request):
    return render(request, "tweet/about.html")

#if request.method == "GET":
def getTweet(request):
    #QuerySetをjsonに変換  json.dumps()だとダメ
    tweets = list(Post.objects.all().values()) 
    for i in range(len(tweets)):
        tweets[i]["date_posted"] = str(tweets[i]["date_posted"])

    return HttpResponse(json.dumps({"tweets": json.dumps(tweets)})) 

def postTweet(request):

    request = json.loads(request.body.decode())
    #posted_dateとlikesは省略(自動で追加してくれる)
    newPost = Post(content = request["content"], author = request["author"])
    #勝手にレコードにidが割り振られる
    newPost.save()

    return HttpResponse(json.dumps({"id": list(Post.objects.all().values())[-1]["id"]}))
    
def addLikeCount(request):

    request = json.loads(request.body.decode())
    #<<カラム名>>__contains = 値 -> where カラム名 == 値
    Post.objects.filter(id__contains = request["id"]).update(likes = request["likes"] + 1)

    return HttpResponse(json.dumps({"message": ""})) 

def deleteTweet(request):

    request = json.loads(request.body.decode())
    Post.objects.filter(id__contains = request["id"]).delete()
    return HttpResponse(json.dumps({"message": ""})) 

