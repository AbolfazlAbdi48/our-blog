from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='account/avatar/', null=True, blank=True, verbose_name='تصویر پروفایل')

    def get_avatar(self):
        return format_html(f"<img width=75 height=75 style='border-radius: 5px;' src='{self.avatar.url}'>")

    get_avatar.short_description = "تصویر پروفایل"
