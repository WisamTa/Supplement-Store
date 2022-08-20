from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    """
    class for review admin configuration
    """
    list_display = (
        'rating',
        'review_text',
        'product',
        'user',
        'date'
    )

    ordering = ('product', )


admin.site.register(Review, ReviewAdmin)
