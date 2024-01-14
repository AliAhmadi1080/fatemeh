from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from blog.models import Blog
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), help_text='برای اطلاع از ایجاد وبلاگ جدید')
