# Generated by Django 3.1.1 on 2020-10-30 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20201030_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('НОВОСТИ', 'НОВОСТИ'), ('АНАЛИТИКА', 'АНАЛИТИКА')], default='АНАЛИТИКА', max_length=20, verbose_name='Категория'),
        ),
    ]
