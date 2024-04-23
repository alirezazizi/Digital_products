from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):

    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    discription = models.TextField(_('discription'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True)
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('create time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update'), auto_now=True)

    class Meta:

        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product (models.Model):

    title = models.CharField(_('title'), max_length=50)
    discription = models.TextField(_('discription'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('category', verbose_name='categories', blank=True)
    created_time = models.DateTimeField(_('create time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update'), auto_now=True)

    class Meta:

        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class File(models.Model):

    prodcut = models.ForeignKey('Product', verbose_name='products', on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField('file', upload_to='file/%Y/%M/%d/')
    created_time = models.DateTimeField(_('create time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update'), auto_now=True)

    class Meta:

        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'
