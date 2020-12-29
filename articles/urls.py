from django.urls import path
from .import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about-us/", views.about_us, name="about_us"),
    path("news/", views.NewsView.as_view(), name="news"),
    path("analytica/", views.AnalyticaView.as_view(), name="analytica"),
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("contacts/", views.contacts, name="contacts"),
    path("archive/", views.archive, name="archive"),
    path("archive/<slug:slug>/", views.ArchiveDetailView.as_view(), name="archive_detail"),
    path("poll-archive/", views.poll_archive, name="poll_archive"),
    path("poll-archive/<slug:slug>/", views.PollDetailView.as_view(), name="poll_detail"),
]

