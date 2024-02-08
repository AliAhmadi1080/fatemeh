from django.shortcuts import render
from blog.models import Blog
# Create your views here.

def aboutpage(request):
    return render(request, 'pages/about.html')
def contactpage(request):
    return render(request,'pages/contact.html')

def homepage(request):
    a = Blog.objects.all()[:5]
    return render(request,'base.html',{'blogs':a})

def detaleblog(request,pk):
    a = Blog.objects.get(id=pk)

    return render(request,'pages/blogdetaile.html',{'blogdetale':a})

def allblog(request):
    a = Blog.objects.all()
    context = {'bloglist':a}
    print(a, context)
    return render(request, 'pages/bloglist.html', context)