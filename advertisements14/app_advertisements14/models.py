from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisements14(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если возможен торг')
    connection = models.BooleanField('Связь', help_text='Отметьте, если возможна связь с продавцом', default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_time.date() == timezone.now().date():
            created_time_2 = self.created_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time_2
            )
        return self.created_time.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_time.date() == timezone.now().date():
            updated_time_2 = self.updated_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time_2
            )
        return self.updated_time.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f'Advertisements14(id={self.id}, title={self.title}, price={self.price}'
    class Meta:
        db_table = 'advertisements'