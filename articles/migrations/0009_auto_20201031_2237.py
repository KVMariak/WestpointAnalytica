# Generated by Django 3.1.1 on 2020-10-31 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_question_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('АНАЛИТИКА', 'АНАЛИТИКА'), ('НОВОСТИ', 'НОВОСТИ')], default='АНАЛИТИКА', max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(default='', max_length=500, verbose_name='Описание'),
        ),
    ]