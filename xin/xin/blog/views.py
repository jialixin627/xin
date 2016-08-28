from django.shortcuts import render
from xin.blog.models import Article
from django.template.response import TemplateResponse

# Create your views here.

def blog(request):
    article = Article.objects.first()
    context = {'article': article}
    return TemplateResponse(request, 'blog/index.html', context)