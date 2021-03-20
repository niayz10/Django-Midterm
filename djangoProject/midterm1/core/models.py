from django.db import models
from utils.constants import Type_ROLES, Type_Food


# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateField(verbose_name='Дата создания')

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')
    genre = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=Type_ROLES, default=Type_Food)
    publisher = models.CharField(max_length=255, null=True, blank=True, verbose_name='Издатель')
