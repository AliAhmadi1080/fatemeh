from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Like,Comment
from django.conf import settings

from django.core.mail import send_mail


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
        
    
@receiver(post_save,sender=Comment)
def sendemail(created,instance,**kwarg):
    if created:
        blog = instance.blog
        subject = 'Fatemeh site'
        message = f'comment for this Blog: "{blog.titel}" '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail( subject, message, email_from, recipient_list
                  ,fail_silently=False, auth_user=None
                  , auth_password=None, connection=None
                  , html_message=None)