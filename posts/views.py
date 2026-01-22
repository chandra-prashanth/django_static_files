from django.shortcuts import render
from django.http import HttpResponse,HttpRequest


posts = [
    {
        "id":1,
        "title":"Learn Django",
        "author":"Ssali Jonath"
    },
    {
        "id":2,
        "title":"Learn Python",
        "author":"Ssali Jonath"
    },
    {
        "id":3,
        "title":"Learn Javascript for brigneers",
        "author":"Ssali Jonath"
    },
]


# Create your views here.
def index(request:HttpRequest):
    name = request.GET.get("name") or "World"
    context = {
        "name":name,
        "posts":posts,
        "title":"Home Page"
    }
    return render(request,'index.html',context)

def about(request):
    context={
        "title":"About Page"
    }
    return render(request,'about.html',context)

def services(request):
    context={
        "title":"services page"
    }
    return render(request,'services.html',context)

def greet(request:HttpRequest):
    name = request.GET.get("name") or "World"
    return HttpResponse(f"Hello {name}")

def return_all_posts(request:HttpRequest):
    return HttpResponse(str(posts))


def return_one_post(request:HttpRequest,post_id):
    for post in posts:
        if post["id"]==post_id:
            return HttpResponse(str(post))
        
    return HttpResponse("Not Found")