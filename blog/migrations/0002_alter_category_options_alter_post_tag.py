# Generated by Django 4.1.7 on 2023-03-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(related_name="posts", to="blog.tag"),
        ),
    ]