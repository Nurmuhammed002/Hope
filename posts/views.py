from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm, PostForm2, CommentForm
import random


def test_view(request):
    return HttpResponse(f"Hello World!{random.randint(0,1000)}")


def main_page_view(request):
    if request.method == "GET":
       return render(request,'base.html')


def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        form = CommentForm()
        comment = post.comments.all()
        return render(request, "posts/post_detail.html", context={"post": post, "form": form, "comments": comment})


    if request.method == "POST":
        forms = CommentForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "posts/post_detail.html",
                context={"post": post, "form": form}
            )
        text = forms.cleaned_data["text"]
        Comment.objects.create[text=text, post=post]
        return redirect(f"/posts/{post.id}/")


def post_create_view(request,):
    if request.method == "GET":
        form = PostForm2()
        return render(request,"posts/post_create.html", context={"form":form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form":form})
        form.save()
        return redirect("/posts/")




