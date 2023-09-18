from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='image_post/', verbose_name='постер')
    created = models.DateTimeField(auto_now_add=True, verbose_name='время создание')
    category = models.ForeignKey('posts.Category', models.CASCADE, verbose_name='категория', null=True)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def get_absolute_url(self):
        return reverse("new_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f'{self.title}'    
    

class Category(models.Model):
    
    title = models.CharField(max_length=50, verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')
    url = models.SlugField(max_length=50, verbose_name='путь')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.url})
    
    def __str__(self) -> str:
        return f'{self.title}'    
    
    
class PostPart(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='под заголовок')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='image_post/', verbose_name='Фото')
    
    
    def __str__(self) -> str:
        return f'{self.title}'   