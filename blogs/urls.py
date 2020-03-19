from django.urls import path
from django.contrib import admin
from . import views

app_name= "blogs"

urlpatterns=[
    path ("", views.MainPage, name= "main_page"),

    path ("<int:author_id>/", views.AuthorDetail, name= "author_detail"),
    path ("<int:author_id>/<int:blog_id>/", views.BlogDetail, name= "blog_detail"),
    path ("all_blogs/", views.ViewAllBlog, name= "view_all_blog"),

    path ("<int:author_id>/create_blog", views.CreateBlog, name= "create_blog"),
    path ("<int:author_id>/create_blog/make_blog", views.MakeBlog, name= "make_blog"),

    path ("<int:author_id>/<int:blog_id>/comments", views.CreateComments, name= "create_comment"),
    path ("<int:author_id>/<int:blog_id>/comments/make_comment", views.MakeComment, name= "make_comment"),

    path ("create_author/", views.CreateAuthor, name= "create_author"),
    path ("create_author/make_author/", views.MakeAuthor, name= "make_author")
]