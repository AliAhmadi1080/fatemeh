from django.urls import path
from .views import homepage, detaleblog, allblog, contactpage, aboutpage


urlpatterns = [
    path('',homepage,name='homepage'),
    path('<int:pk>/',detaleblog,name='detaileblog'),
    path('all/', allblog, name='allblog'),
    path('contact',contactpage,name='contact'),
    path('about',aboutpage,name='about'),
]

