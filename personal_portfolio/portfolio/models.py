from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)  #Название, параметр максимальная длина 100 символов
    description = models.CharField(max_length=250) #описание, параметр максимальная длина 250 символов
    image = models.ImageField(upload_to='portfolio/images/') # Изображение параметр сохранения в указанную дирректорию
    url = models.URLField(blank=True)   # Ссылка, параметр отвечает за открытие в новой вкладке

