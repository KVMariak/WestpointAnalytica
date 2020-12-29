# Generated by Django 3.1.1 on 2020-10-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20201031_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='availability',
            field=models.BooleanField(default=False, verbose_name='Активный'),
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('Активный', 'Активный'), ('Не активнен', 'Не активен')], default='Не активнен', max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('НОВОСТИ', 'НОВОСТИ'), ('АНАЛИТИКА', 'АНАЛИТИКА')], default='АНАЛИТИКА', max_length=20, verbose_name='Категория'),
        ),
    ]