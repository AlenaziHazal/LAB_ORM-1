# Generated by Django 4.2.7 on 2023-11-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blogs_catagory_blogs_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='catagory',
            field=models.CharField(choices=[('Action', 'Action'), ('Fantacy', 'Fantacy'), ('Horror', 'Horror'), ('Romantic', 'Romantic')], max_length=1028),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='images',
            field=models.ImageField(default='images.jpg', upload_to='media/images'),
        ),
    ]