# Generated by Django 5.1 on 2024-08-10 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news_post',
            old_name='pub_date',
            new_name='date',
        ),
    ]
