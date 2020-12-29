# Generated by Django 3.1.1 on 2020-10-30 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201026_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='Вариант ответа')),
                ('votes', models.IntegerField(default=0, verbose_name='Голосов')),
            ],
            options={
                'verbose_name': 'Составляющие опроса',
                'verbose_name_plural': 'Составляющие опросов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='Название')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.RemoveField(
            model_name='polloption',
            name='poll',
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('АНАЛИТИКА', 'АНАЛИТИКА'), ('НОВОСТИ', 'НОВОСТИ')], default='АНАЛИТИКА', max_length=20, verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='PollOption',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.question'),
        ),
    ]
