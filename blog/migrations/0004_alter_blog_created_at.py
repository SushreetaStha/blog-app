# Generated by Django 4.1.7 on 2023-03-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_tags_blog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(verbose_name='date published'),
        ),
    ]