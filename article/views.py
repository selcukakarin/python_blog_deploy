from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from article.forms import ArticleForm
from article.models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse


# Create your views here.


def index(request):
    users = User.objects.all()
    mylist = []
    for user in users:
        mylist.append(user.first_name)

    context = {
        "users": users,
        "mylist": mylist,
        "isim": "Ali",
        "yas": 18,
        "numbers": [1, 2, 3, 4, 5, 6, 7, 8],
        "coffees": {"latte": 25, "americano": 30, "çay": 15, "filtre kahve": 35}
    }
    return render(request, "index.html", context)


def index2(request):
    return render(request, "index2.html")


def about(request):
    return render(request, "about.html")


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    # article = Article.objects.filter(id=id).first()
    comments = article.comments.all()
    context = {
        "article": article,
        "comments": comments
    }
    return render(request, "detail.html", context)


# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="user:login")
def create(request):
    return render(request, "create.html")


def frontend_test(request):
    users = User.objects.all()
    return render(request, "frontend.html", {"users": users})


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
        "site_admini": "selçuk akarın",
        "location": "istanbul",
        "meyveler": ["Elma", "Armut", "Vişne", "Hindistan Cevizi"]
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addArticle(request):
    # Post request
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # author = form.cleaned_data.get("author")
        # title = form.cleaned_data.get("title")
        #
        # article = Article()
        # article.author = author
        # article.title = title
        # article.save()

        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makaleniz başarıyla kaydedildi.")
        return redirect("article:dashboard")

    context = {
        "form": form
    }
    return render(request, "addArticle.html", context)


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()  # commit = True

        messages.success(request, "Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()

    messages.success(request, "Makele başarıyla silindi.")
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword")
    articles = Article.objects.all()
    if keyword:
        articles = Article.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword))

    return render(request, "articles.html", {"articles": articles})


def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        new_comment = Comment()
        new_comment.comment_author = comment_author
        new_comment.comment_content = comment_content
        new_comment.article = article
        new_comment.save()
    return redirect(reverse("article:detail", kwargs={"id": id}))
