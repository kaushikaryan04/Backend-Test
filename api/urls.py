from django.urls import path
from .views import CreateBlog , ShowAllBlogs ,ShowBlog ,UpdateBlog
urlpatterns = [
    path("create" , CreateBlog.as_view()),
    path("all" , ShowAllBlogs.as_view() ),
    path("list/<int:blogId>" , ShowBlog.as_view() ),
    path("update/<int:blogId>" ,UpdateBlog.as_view() )
]