# Generated by Django 4.0.3 on 2022-08-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_ticket_created_ticket_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='defaultpics/profdefault.jpg', null=True, upload_to='account/avatar/', verbose_name='تصویر پروفایل'),
        ),
    ]
