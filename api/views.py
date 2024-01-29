from django.shortcuts import render
from .serialaizer import BlogSerializer
from blog.models import Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def allblogapi(request):
    a = Blog.objects.all()
    sa = BlogSerializer(a,many=True)
    return Response(sa)