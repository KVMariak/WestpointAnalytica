from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Region, Articles, Question, Choice, Feedback, Year

# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticlesAdminForm(forms.ModelForm):
    long_description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Articles
        fields = '__all__'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    fieldsets = [(None, {'fields': ['question_text', 'status', 'availability', 'description', 'pub_date', 'url']})]
    inlines = [ChoiceInline]


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published", "region", "get_image")
    list_filter = ("category",)
    search_fields = ("title",)
    form = ArticlesAdminForm
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" height="90"')

    get_image.short_description = "Изображение"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    readonly_fields = ("name", "email", "text")


admin.site.register(Region)
admin.site.register(Year)

