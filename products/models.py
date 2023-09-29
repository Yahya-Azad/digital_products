from django.db import models
from django.utils.translation import gettext_lazy as _


# gettext for views

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    # it's foreign key       for subcategory           به یک رکورد خاص
    title = models.CharField(verbose_name=_('title'), max_length=50)  # usually it's first parameter
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    create_time = models.DateTimeField(_('created time '), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time '), auto_now=True)

    class Meta:   # for extra attribute
        db_table = 'categories'  # default app_model but we modified it
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    create_time = models.DateTimeField(_('created time '), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time '), auto_now=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)  # به چند رکورد خاص
    # یکی از product ها با برای بیشتر از یک category باشه

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey('product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')  # directory for days
    is_enable = models.BooleanField(_('is enable'), default=True)
    create_time = models.DateTimeField(_('created time '), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time '), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
