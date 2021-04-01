from django.contrib import admin
from .models import Ebook, Category, Ebook_reader

# Register your models here.


class EbookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'category',
        'authors',
        'year',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class Ebook_readerAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'brand',
        'model',
        'size',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Ebook, EbookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ebook_reader, Ebook_readerAdmin)
