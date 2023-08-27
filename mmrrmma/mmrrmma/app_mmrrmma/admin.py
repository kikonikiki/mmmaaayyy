from django.contrib import admin
from .models import Mmrrmma
from django.db import models
from django.utils.html import format_html

class MmrrmmaAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'price', 'created_date',  'auction', 'updated_date', 'image',]

    list_filter = ['auction', 'created_at']


    actions = ['make_auctions_as_false', 'make_auction_as_true']


    fieldsets = (
        ('Общее',{
            'fields': ('title', 'description', 'image', 'user'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    # @admin.display(ordering='first_name')
    # def colored_first_name(self):
    #     return format_html(
    #         '<span style="color: #{};">{}</span>',
    #         self.color_code,
    #         self.first_name,
    #     )

admin.site.register(Mmrrmma, MmrrmmaAdmin)
