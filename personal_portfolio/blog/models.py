
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)  #Название, параметр максимальная длина 100 символов
    description = models.TextField() #описание, параметр максимальная длина 250 символов
    date = models.DateField(null=True)

    def __str__(self):
        return self.title #Для отображения названия блога в админке а не блог №1