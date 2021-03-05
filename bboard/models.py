from django.db import models

# Create your models here.
# ТОВАРЫ - ЭТО БУДЕТ ВТОРИЧНАЯ МОДЕЛЬ 
class Bb (models.Model):  # Модель - подкласс класса Model
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    pablished = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name_plural = "ОБЪЯВЛЕНИЯ"
        verbose_name = "Объявление :"
        ordering = ["-pablished"]

# РУБРИКИ ЭТО БУДЕТ ПЕРВИЧНАЯ МОДЕЛЬ 
class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']