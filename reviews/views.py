from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import Add_ReviewForm


@login_required
def add_review(request, product_id):
    """
     View to add reviews
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = Add_ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. \
                Please ensure all form fields are valid')
    else:
        form = Add_ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required()
def delete_review(request, product_id, review_id):
    """
    Allow admin to delete user reviews
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    review = Review(product=product, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
