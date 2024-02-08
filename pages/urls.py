from django.urls import path
from .views import homepage, detaleblog, allblog, contactpage


urlpatterns = [
    path('',homepage,name='homepage'),
    path('<int:pk>/',detaleblog,name='detaileblog'),
    path('all/', allblog, name='allblog'),
    path('contact',contactpage,name='contact')
]

