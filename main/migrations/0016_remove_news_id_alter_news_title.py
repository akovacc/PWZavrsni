# Generated by Django 4.1.3 on 2024-09-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_news_category_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="id",
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=25, primary_key=True, serialize=False, verbose_name="Naslov"
            ),
        ),
    ]
