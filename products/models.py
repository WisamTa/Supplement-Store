from django.db import models


class Category(models.Model):
    """
    A class for the category model
    """
    class Meta:
        """
        A class for Meta information
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns the category name string
        """
        return str(self.name)

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    A class for the product model
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
