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
        IPAddress, related_name='articles', blank=True, verbose_name='بازدید ها'
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

    def get_replace_name(self):
        return f"{self.title.replace(' ', '-')}"


class Comment(models.Model):
    """
    The Comment model
    """
    owner = models.ForeignKey(
        User, verbose_name='نظر دهنده', on_delete=models.CASCADE, null=False, blank=False
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

    def __str__(self):
        return f"{self.owner} | {self.article}"


class Like(models.Model):
    """
    The Like model
    """
    owner = models.ForeignKey(
        User, verbose_name='توسط', on_delete=models.CASCADE, null=False, blank=False
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name='مقاله', null=False, blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ لایک'
    )

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

    def __str__(self):
        return f"{self.owner} | {self.article}"


class SaveArticle(models.Model):
    """
    The SaveArticle model
    """
    owner = models.ForeignKey(
        User, verbose_name='توسط', on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Article, verbose_name="مقاله", on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
        )

    class Meta:
        verbose_name = 'ذخیره مقاله'
        verbose_name_plural = 'مقاله های ذخیره شده'

    def __str__(self):
        return f'{self.owner} | {self.article}'
