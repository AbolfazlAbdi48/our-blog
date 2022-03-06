from pyexpat import model
from django.db import models

# Create your models here.


class IPAddress(models.Model):
    """
    The main IPAddress model.
    """
    ip_address = models.GenericIPAddressField(verbose_name='آی پی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')

    class Meta:
        verbose_name = 'آی پی'
        verbose_name_plural = 'آی پی آدرس ها'

    def __str__(self):
        return f"{self.ip_address}"


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=200, verbose_name='دسته بندی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')
    is_deleted = models.BooleanField(default=False, verbose_name='پاک شده/نشده')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.name}'
