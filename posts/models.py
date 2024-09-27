from django.db import models

"""
Posts.objects.all() - достает все обьекты таблицы без исключения
Posts.objects.filter(title="Тестовая запись") - достает только нужные обьекты
Posts.objects.get(title="Тестовая запись") - достает только нужные обьекты
Posts.object.create(title="Тестовая запись", content="Тестовый контент", rate=0) - создает обьект
"""


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
