# Generated by Django 5.0.1 on 2024-02-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='statics/assets/img/about-bg.jpg', upload_to='statics/assets/img', verbose_name='عکس'),
        ),
    ]
