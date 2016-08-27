from django.shortcuts import render
from xin.blog.models import Article
from django.template.response import TemplateResponse

# Create your views here.

def blog(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return TemplateResponse(request, 'blog/index.html', context)