from django.contrib import admin
from .models import Advertisements14

class Advertisements14Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'connection', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description', 'connection')
        }),
        ('Финансы', {
            'fields':('price', 'auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction='False')

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction='True')

admin.site.register(Advertisements14, Advertisements14Admin)
