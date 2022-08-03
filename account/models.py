from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='account/avatar/', null=True, blank=True, verbose_name='تصویر پروفایل', default='defaultpics/profdefault.jpg')

    def get_avatar(self):
        return format_html(f"<img width=75 height=75 style='border-radius: 5px;' src='{self.avatar.url}'>")

    get_avatar.short_description = "تصویر پروفایل"


class Ticket(models.Model):
    subject = models.CharField(max_length=75, verbose_name='موضوع')
    user = models.ForeignKey(
        User, related_name='tickets', on_delete=models.CASCADE, verbose_name='ارسال کننده'
    )
    message = models.TextField(verbose_name='پیام')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ آخرین ویرایش'
    )
    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return f"{self.subject}"
