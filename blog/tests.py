from django.test import TestCase
from blog.models import Blog, Categorys, Comment
from django.contrib.auth.models import User
from datetime import date

class BlogTestCase(TestCase):
    def setUp(self) -> None:
        c1 = Categorys.objects.create(name='c1')
        u1 = User.objects.create(username='user',password='pass')
        b1 = Blog.objects.create(author=u1,titel='titel',sub_titel='sub_titel',text='''
LOREM IPSUM GENERATOR
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
Ut enim ad minim veniam, quis nostrud''',image='statics\assets\img\about-bg.jpg',like_count=0,date=date.today())
        b1.categorys.add(c1)

    def test_blog(self):
        '''test blogs'''
        c1 = Categorys.objects.get(name='c1')
        b1 = Blog.objects.get(titel='titel',text='''
LOREM IPSUM GENERATOR
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
Ut enim ad minim veniam, quis nostrud''')
        self.assertEqual(b1.text,'''
LOREM IPSUM GENERATOR
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
Ut enim ad minim veniam, quis nostrud''')
        self.assertEqual(c1.name,'c1')

class CategorysTestCase(TestCase):
    def setUp(self) -> None:
        c1 = Categorys.objects.create(name='name')

    def test_categorys(self):
        c1 = Categorys.objects.get(name='name')
        self.assertEqual(c1.name,'name')
    
class CommentTestCase(TestCase):
    def setUp(self) -> None:
        u1 = User.objects.create(username='user',password='pass')
        b1 = Blog.objects.create(author=u1,titel='titel',sub_titel='sub_titel',text='''
LOREM IPSUM GENERATOR''',image='statics\assets\img\about-bg.jpg',like_count=0,date=date.today())
        c1 = Comment.objects.create(name='ali',blog=b1,text='This is text. This is a another text')

    def test_comment(self):
        c1 =Comment.objects.get(name='ali')
        self.assertEqual(c1.name,'ali')
        