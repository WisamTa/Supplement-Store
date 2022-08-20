from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    A class for the review model
    """

    choices = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    rating = models.IntegerField(choices=choices, default=1)
    review_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
                             User, on_delete=models.CASCADE,
                             blank=True, null=True, default='')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        blank=True, null=True, default='')

    def __str__(self):
        return str(self.review_text)
