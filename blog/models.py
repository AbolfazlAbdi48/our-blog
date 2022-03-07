from django.utils import timezone
from django.db import models
from django.utils.html import format_html
from account.models import User

# Create your models here.


class IPAddress(models.Model):
    """
    The main IPAddress model.
    """
    ip_address = models.GenericIPAddressField(verbose_name='آی پی')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ آخرین ویرایش'
    )

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
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ آخرین ویرایش'
    )
    is_deleted = models.BooleanField(
        default=False, verbose_name='پاک شده/نشده'
    )
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    """
    The Article model.
    """

    title = models.CharField(max_length=75, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده'
    )
    image = models.ImageField(
        upload_to='articles/', verbose_name='تصویر مقاله'
    )
    hits = models.ManyToManyField(
        IPAddress, related_name='articles', null=True, blank=True, verbose_name='بازدید ها'
    )
    publish_time = models.DateTimeField(
        default=timezone.now, verbose_name='زمان انتشار'
    )
    categories = models.ManyToManyField(
        Category, related_name='articles', verbose_name='دسته بندی ها'
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ آخرین ویرایش'
    )

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return f"{self.title}"

    def get_thumbnail(self):
        return format_html(f"<img width=100 height=75 style='border-radius: 5px;' src='{self.image.url}'>")

    get_thumbnail.short_description = "تصویر"


class Comment(models.Model):
    """
    The Comment model
    """
    owner = models.ForeignKey(
        User, verbose_name='نظر دهنده', null=False, blank=False
        )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name='مقاله', null=False, blank=False
    )
    massage = models.TextField(
        verbose_name='متن نظر', null=False, blank=False
        )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ آخرین ویرایش'
    )

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
