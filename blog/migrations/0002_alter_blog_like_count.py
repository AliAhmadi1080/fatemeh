# Generated by Django 5.0.1 on 2024-01-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='like_count',
            field=models.PositiveIntegerField(auto_created=True, default=0, verbose_name='تعداد لایک'),
        ),
    ]
