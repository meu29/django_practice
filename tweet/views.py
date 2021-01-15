#ファイル名にビューとあるが実際はコントローラーの役割?
from django.http import HttpResponse
import json
from django.shortcuts import render
#from django.views.decorators.csrf import ensure_csrf_cookie
#tweet/models.pyのPostクラスをインポート?
from .models import Post

#@ensure_csrf_cookie

def indexView(request):
    #model = Post
    return render(request, "tweet/index.html")

def aboutView(request):
    return render(request, "tweet/about.html")

def fetch(request):
    if request.method == "GET":
        response = json.dumps({"tweets": [
            {"content": "あああ", "author": "bot", "date_posted": "2020/9/11", "liles": 0},
            {"content": "いいい", "author": "bot", "date_posted": "2020/9/11", "liles": 0},
            {"content": "ううう", "author": "bot", "date_posted": "2020/9/11", "liles": 0},
        ]}) 
    else:
        response = json.dumps({"message": "まんちお！"}) 

    return HttpResponse(response) 
        
