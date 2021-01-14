#ファイル名にビューとあるが実際はコントローラーの役割?
from django.http import HttpResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
#tweet/models.pyのPostクラスをインポート?
from .models import Post

def indexView(request):
    #model = Post
    return render(request, "tweet/index.html")

def aboutView(request):
    return render(request, "tweet/about.html")

@ensure_csrf_cookie
def fetch(request):
    content = request.POST()
    response = json.dumps({"message": "まんちお！"}, ensure_ascii=False, indent=2) 
    return HttpResponse(response) 
        
