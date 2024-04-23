from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Category(models.Model):

    parent = models.ForeignKey('self', verbose_name=('parent'),blank=True,null=True,on_delete=models.CASCADE())
    title = models.CharField(_('title'),max_length=50)
    discription = models.TextField(_('discription'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True)
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('create time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update'),auto_now=True)


    class Meta :

        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
