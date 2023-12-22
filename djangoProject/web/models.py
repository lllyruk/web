from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название',max_length=50)
    task = models.TextField('описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'