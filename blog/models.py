from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categorys(models.Model):
    name = models.CharField(max_length=60,verbose_name='اسم عنوان')

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده')
    titel  = models.CharField(max_length=60,verbose_name='عنوان')
    sub_titel = models.CharField(max_length=150,verbose_name='زیر عنوان')
    date = models.DateField(auto_created=True,auto_now_add=True,verbose_name='زمان')
    categorys = models.ManyToManyField('Categorys',verbose_name='دسته بندی')
    text = models.TextField(verbose_name='متن اصلی')
    like_count = models.PositiveIntegerField(default=0,auto_created=True,verbose_name='تعداد لایک')


    def __str__(self) -> str:
        return f'{self.author} , {self.titel}'
    
    def get_absolute_url(self):       
        return reverse('detaileblog', args=[str(self.pk)])
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.user} -> {self.blog}'
    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} -> {self.is_liked}'