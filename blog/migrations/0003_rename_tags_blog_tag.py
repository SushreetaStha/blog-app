# Generated by Django 4.1.7 on 2023-03-30 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_content_remove_blog_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tags',
            new_name='tag',
        ),
    ]
