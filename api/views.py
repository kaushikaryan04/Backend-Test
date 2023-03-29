from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializers
# show all blogs
class ShowAllBlogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


#update blog based on id
class UpdateBlog(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "blogId"

# see one blog according to id
class ShowBlog(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "blogId"

#create a blog
class CreateBlog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

