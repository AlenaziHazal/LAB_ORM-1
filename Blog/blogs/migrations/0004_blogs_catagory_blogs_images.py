# Generated by Django 4.2.7 on 2023-11-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogs_published_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='catagory',
            field=models.CharField(default='Action', max_length=1028),
        ),
        migrations.AddField(
            model_name='blogs',
            name='images',
            field=models.ImageField(default='images.jpg', upload_to=''),
        ),
    ]
