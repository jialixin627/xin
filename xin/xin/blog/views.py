from django.shortcuts import render
from xin.blog.models import Article
from django.template.response import TemplateResponse
from django.shortcuts import render

# Create your views here.

def blog(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)