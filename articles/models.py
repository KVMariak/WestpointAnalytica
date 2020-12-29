from django.db import models
from django.urls import reverse


class Region(models.Model):
    """Region fields"""
    name = models.CharField("Регион", max_length=100)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Articles(models.Model):
    """Article fields"""
    ANALYTICA = 'АНАЛИТИКА'
    NEWS = 'НОВОСТИ'

    CHOICE_GROUP = {
        (ANALYTICA, 'АНАЛИТИКА'),
        (NEWS, 'НОВОСТИ')
    }

    title = models.CharField("Название", max_length=100)
    short_description = models.TextField("Краткое описание")
    long_description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="articles/")
    published = models.DateTimeField("Дата публикации", auto_now=False, auto_now_add=False, blank=True)
    category = models.CharField(max_length=20, verbose_name="Категория", choices=CHOICE_GROUP, default=ANALYTICA)
    region = models.ForeignKey(Region, verbose_name="Регион", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Question(models.Model):
    """Poll question fields"""
    ACTIVE = 'Активный'
    INACTIVE = 'Не активнен'

    CHOICE_GROUP = {
        (ACTIVE, 'Активный'),
        (INACTIVE, 'Не активен')
    }

    question_text = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=500, default='')
    status = models.CharField(max_length=20, verbose_name="Статус", choices=CHOICE_GROUP, default=INACTIVE)
    availability = models.BooleanField("Активный", default=False)
    pub_date = models.DateTimeField("Дата публикации")
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(models.Model):
    """Component of poll fileds"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Вариант ответа", max_length=200)
    votes = models.IntegerField("Голосов", default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Составляющие опроса"
        verbose_name_plural = "Составляющие опросов"


class Feedback(models.Model):
    """Feedback fields"""
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    text = models.TextField("Сообщение", max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Письма читателей"


class Year(models.Model):
    """Archive year fields"""
    name = models.CharField("Название", max_length=100, default='')
    year_name = models.IntegerField("Год", default=0)
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Архив по годам"
        verbose_name_plural = "Архив по годам"

