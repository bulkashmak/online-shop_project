from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductFrom


@require_POST
def cart_add(request, product_id):
    """
    Adds products to the cart or updating quantities for
    existing products.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductFrom(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:car_detail')


@require_POST
def cart_remove(product_id, request):
    """
    Receives the product ID as a param. Retrieve the Product
    instance with the given ID and remove the product from the
    cart. Then redirect the user to cart_detail URL
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """
    Gets the current cart to display it.
    """
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
