from django.shortcuts import render
from django.views import View

from .models import *


# Create your views here.

class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        last_three_posts = Post.objects.all().order_by('-pk')[:3]
        context = {
            "posts": posts,
            "categories": categories,
            'tags': tags,
            'last_three_posts': last_three_posts,
        }
        return render(request, "index.html", context=context)
