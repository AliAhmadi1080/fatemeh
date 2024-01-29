from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fileds = '__all__'
        model = Blog