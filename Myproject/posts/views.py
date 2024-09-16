from django.shortcuts import render
from . models  import Post
# Create your views here.
def post_list(request ):
    Posts=Post.objects.all().order_by("-date") #-add to show it is in descending 
    return render(request, 'posts/post_list.html',{'posts':Posts})
