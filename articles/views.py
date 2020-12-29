import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.core.paginator import Paginator

from .models import Articles, Feedback, Question, Choice, Year


class IndexView(View):
    """Home page"""
    def get(self, request):
        home_top = Articles.objects.all().order_by("-published")[0:1]
        latest_news_block_1 = Articles.objects.filter(category='НОВОСТИ').order_by("-published")[1:3]
        latest_news_block_2 = Articles.objects.filter(category='НОВОСТИ').order_by("-published")[3:5]
        latest_analytica = Articles.objects.all().filter(category='АНАЛИТИКА').order_by("-published")[0:3]
        latest_poll = Question.objects.last()
        return render(request, "articles/index.html", {'home_top': home_top,
                                                       'latest_news_block_1': latest_news_block_1,
                                                       'latest_news_block_2': latest_news_block_2,
                                                       'latest_analytica': latest_analytica,
                                                       'latest_poll': latest_poll})


def about_us(request):
    """About us page"""
    return render(request, "articles/about_us.html")


class NewsView(View):
    """News page list"""
    def get(self, request):
        news_top = Articles.objects.all().filter(category='НОВОСТИ').order_by("-published")[0:1]
        news_list = Articles.objects.all().filter(category='НОВОСТИ').order_by("-published")[1:]
        paginator = Paginator(news_list, 9)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        return render(request, "articles/news.html", {'news_top': news_top,
                                                      'news_list': page,
                                                      'is_paginated': is_paginated,
                                                      'next_url': next_url,
                                                      'prev_url': prev_url})


class AnalyticaView(View):
    """Analytica page list"""
    def get(self, request):
        analytica_list = Articles.objects.all().filter(category='АНАЛИТИКА').order_by("-published")
        paginator = Paginator(analytica_list, 6)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        return render(request, "articles/analytica.html", {'analytica_list': page,
                                                           'is_paginated': is_paginated,
                                                           'next_url': next_url,
                                                           'prev_url': prev_url})


class ArticleDetailView(View):
    """Detailed description of a article page"""
    def get(self, request, slug):
        article = Articles.objects.get(url=slug)
        today = datetime.datetime.now()
        random_article = Articles.objects.all().filter(published__month=today.month).order_by('?')[:2]
        return render(request, "articles/single.html", {"article": article,
                                                        "random_article": random_article})


def contacts(request):
    """Contacts page. The feedback form is stored in the database."""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        form = Feedback(name=name, email=email, text=text)
        form.save()
    return render(request, "articles/contacts.html")


def poll_archive(request):
    """Poll list"""
    poll_archive_list = Question.objects.all().order_by("-pub_date")
    paginator = Paginator(poll_archive_list, 9)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    return render(request, "articles/poll_archive.html", {'poll_archive_list': page,
                                                          'is_paginated': is_paginated,
                                                          'next_url': next_url,
                                                          'prev_url': prev_url})


class PollDetailView(View):
    """Detail of a poll"""
    def get(self, request, slug):
        poll = Question.objects.get(url=slug)
        return render(request, "articles/single_poll.html", {"poll": poll})


def archive(request):
    """Archive of analytical articles"""
    archive_year = Year.objects.all()
    return render(request, "articles/archive.html", {'archive_year': archive_year})


class ArchiveDetailView(View):
    """Detail archive"""
    def get(self, request, slug):
        year = Year.objects.get(url=slug)
        archive_articles = Articles.objects.all().filter(category='АНАЛИТИКА').order_by("-published")[0:]
        return render(request, "articles/archive_year.html", {"year": year,
                                                              'archive_articles': archive_articles})

