from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Author, BlogPost, Comments
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def MainPage (request):
    author_list = Author.objects.all()
    return render (request, "blogs/main_page.html", context= {"author_list": author_list})

def BlogDetail (request, blog_id, author_id):
    author = get_object_or_404 (Author, pk= author_id)
    blog = get_object_or_404 (author.blogpost_set, pk = blog_id)
    commnet_list = blog.comments_set.all()

    return render (request, "blogs/blog_detail.html", context= {"blog": blog, 
                                                                "comment_list": commnet_list,})

def AuthorDetail (request, author_id):
    author = get_object_or_404 (Author, pk= author_id)
    blog_list = BlogPost.objects.filter (author= author)
    return render(request, "blogs/author_detail.html", context= {"author": author,
                                                                 "blog_list": blog_list,})

def CreateBlog (request, author_id):
    author = get_object_or_404 (Author, pk= author_id)
    return render (request, "blogs/create_blog.html", context= {"author": author})

def MakeBlog (request, author_id):
    author = get_object_or_404 (Author, pk= author_id)
    new_blog = BlogPost (author= author, 
                        pub_date= timezone.now(), 
                        title= request.POST["blog_title"], 
                        blog_text= request.POST["blog_text"])

    new_blog.save()

    return HttpResponseRedirect (reverse("blogs:create_blog", args= [author_id]))

def CreateComments (request, blog_id, author_id):
    author = get_object_or_404 (Author, pk= author_id)
    return render (request, "blogs/create_comment.html", context= {"author_id": author_id,
                                                             "blog_id": blog_id,})

def MakeComment (request, author_id, blog_id):
    author = Author.objects.get (pk= author_id)
    blog = BlogPost.objects.get (pk= blog_id)
    new_comment = Comments (commentor= request.POST["commentor_name"],
                            blog= blog,
                            comment_text= request.POST["comment_text"],)
    new_comment.save()
    return HttpResponseRedirect (reverse("blogs:create_comment", args= [author_id, blog_id]))

def ViewAllBlog (request):
    blog_list = BlogPost.objects.all()
    return render (request, "blogs/all_blogs.html", context= {"blog_list": blog_list})

def CreateAuthor (request):
    return render (request, "blogs/create_author.html",)

def MakeAuthor (request):
    new_author = Author (name= request.POST["author_name"],
                         join_date= timezone.now(),
                         details= request.POST["author_description"])
    new_author.save()
    return HttpResponseRedirect (reverse("blogs:create_author", args= []))
