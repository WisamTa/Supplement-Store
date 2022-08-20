from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for the Product model.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'image_url',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for the Category model.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
