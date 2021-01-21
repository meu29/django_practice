#ファイル名にビューとあるが実際はコントローラーの役割?
from django.http import HttpResponse
import json
from django.shortcuts import render
#tweet/models.pyのPostクラスをインポート?
from .models import Post
from janome.tokenizer import Tokenizer
import re
import urllib.parse

def indexView(request):
    return render(request, "tweet/index.html")

#if request.method == "GET":
def getTweet(request):

    tokenizer = Tokenizer()
    wordDic = {}

    if re.search(r"keyword=", request.get_full_path()) != None:
        keyword = urllib.parse.unquote(request.get_full_path().split("keyword=")[1])
        tweets = list(Post.objects.filter(content__contains = keyword).values())
    else:
        tweets = list(Post.objects.all().values())

    for i in range(len(tweets)):
        tweets[i]["date_posted"] = str(tweets[i]["date_posted"])#trends
        for token in tokenizer.tokenize(tweets[i]["content"]):
            if len(token.surface) < 3 and re.match(r"[一-龥]+", token.surface) == None:
                pass
            elif token.surface not in wordDic:
                wordDic[token.surface] = 1
            else:
                wordDic[token.surface] += 1
    
    #5回以上使用された単語の内回数が多いもの
    trends = [tupleItem for tupleItem in sorted(wordDic.items(), key=lambda x:x[1], reverse=True) if tupleItem[1] >= 5]
    return HttpResponse(json.dumps({"tweets": json.dumps(tweets), "trends": trends})) 

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

