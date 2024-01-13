from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Like,Blog

@receiver(post_save,sender=Like)
def addlike(created,instance,**kwarg):
    print((instance))
    blog = instance.blog
    print(blog)
    if instance.is_liked == True:
        blog.like_count += 1
        blog.save()

    if instance.is_liked == False:
        blog.like_count -= 1
        blog.save()
        
    
