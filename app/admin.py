from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import *

class PriceListFilter(admin.SimpleListFilter):
    title = 'Price category'
    parameter_name = 'price'
    
    def lookups(self, request, model_admin):
        return(
            ('low', 'Low price'),
            ('medium', 'Medium price'),
            ('high', 'high price'),
        )
        
    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=100)
        elif self.value() == 'medium':
            return queryset.filter(price__gt=100, price__lte=500)
        elif self.value() == 'high':
            return queryset.filter(price__gt=500)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'textile')
    fields = (('name', 'price'), 'textile')
    readonly_fields = ('textile',)
    search_fields = ('name', 'price')
    list_display_links = ('textile',)
    listl_editable = ('name', 'price')
    list_filter = ('textile',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Textile)
admin.site.register(Size)
admin.site.register(Color)
