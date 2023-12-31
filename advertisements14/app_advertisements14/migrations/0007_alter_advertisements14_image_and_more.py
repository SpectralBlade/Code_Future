# Generated by Django 4.2.3 on 2023-08-14 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisements14', '0006_alter_advertisements14_auction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements14',
            name='image',
            field=models.ImageField(default='static/img/adv.png', upload_to='advertisements/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='advertisements14',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
