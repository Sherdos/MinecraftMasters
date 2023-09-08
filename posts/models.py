from django.db import models

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='image_post/', verbose_name='постер')
    created = models.DateTimeField(auto_now_add=True, verbose_name='время создание')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self) -> str:
        return f'{self.title}'    