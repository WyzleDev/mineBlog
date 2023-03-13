from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(_("Название"), max_length=32, null=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(_("Название"), max_length=32, null=False)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Link(models.Model):
    link_to = models.CharField(_("Название соцсети"), max_length=64)
    link = models.URLField()

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return self.link_to


class Post(models.Model):
    image = models.ImageField(_("Картинка"), upload_to="media/")
    tag = models.ManyToManyField(Tag, related_name="posts")
    category = models.ManyToManyField(Category)
    header = models.CharField(_("Название"), max_length=128, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now=True)
    body = models.TextField()
    social_links = models.ManyToManyField(Link)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.header}"


class Advertisement(models.Model):
    header = models.CharField(_("Заголовок объявления"), max_length=128)
    call_to_action_header = models.CharField(_("Текст призыва к действию"), max_length=128)
    link = models.URLField()

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Реклама"

    def __str__(self):
        return f"{self.header}"
