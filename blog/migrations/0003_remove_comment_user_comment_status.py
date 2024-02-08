# Generated by Django 5.0.1 on 2024-02-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('checking', 'Checking'), ('rejected', 'Rejected'), ('published', 'Published')], default='checking', max_length=9),
        ),
    ]