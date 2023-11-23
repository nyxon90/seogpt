import ast
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputKeywords
from .tools import GetArticleThread
from .models import Articles


def index(request):
    return HttpResponse('Hello, word')


def home(request):
    return render(request, "home.html")


def copywriting(request):
    if request.method == 'POST':
        form = InputKeywords(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            user_id = request.user.id

            GetArticleThread(input_text, user_id).start()

            context = {'status': 'Статья создается.'}
        else:
            errors = form.errors
            context = {'errors': errors}
    else:
        form = InputKeywords()
        context = {}
    return render(request, "copywriting/create_article.html", {'form': form, **context})


def copywriting_articles(request):
    articles = Articles.objects.filter(user_id=request.user.id)
    return render(request, 'copywriting/articles.html', {'articles': articles})


def article_detail(request, article_id):
    try:
        article = Articles.objects.get(pk=article_id)
        structure_paragraphs = ast.literal_eval(article.structure)
        content_paragraphs = ast.literal_eval(article.content)

        context = {
            'article': article,
            'structure_paragraphs': structure_paragraphs,
            'content_paragraphs': content_paragraphs,
        }
    except Articles.DoesNotExist:
        context = {'Error': ''}

    return render(request, 'copywriting/article_detail.html', context)

