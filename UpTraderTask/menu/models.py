from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name   = models.CharField(
        max_length=100
        )
    slug   = models.SlugField(
        'Название URL',
        max_length=100,
        )
    parent = TreeForeignKey('self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Родительская категория',
        related_name='children',
        db_index=True
        )
    
    state = models.ForeignKey(
        'Option',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        )
    
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return '{}, {}'.format(
            self.name,
            self.slug,
            )

    def get_absolute_url(self):
        return reverse('menu-item', kwargs={'slug': self.slug})

class Option(models.Model):
    config_name = models.CharField(
        max_length=100
        )
    expanded = models.BooleanField(
        verbose_name='развернутый элемент',
        default=False,
        null=True,
        blank=True,
        )
    
    checked = models.BooleanField(
        verbose_name='активный элемент',
        default=False,
        null=True,
        blank=True,
        )
    
    def __str__(self):
        return self.config_name

class Post(models.Model):
    category    = models.ForeignKey(
        'Menu',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        )
    title       = models.CharField(max_length=120)
    content     = models.TextField(max_length=1200)
    slug        = models.SlugField()

    def __str__(self):
        return self.title