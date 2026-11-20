
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .cart import get_cart
from django.views.decorators.http import require_POST
from django.shortcuts import redirect



def product_list(request):
    products = Product.objects.filter(is_available=True, stock__gt=0)
    return render(request, "shop/product_list.html", {"products": products})


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("shopping_cart", {})
    key = str(product.id)
    cart[key] = cart.get(key, 0) + 1
    request.session["shopping_cart"] = cart

    return redirect("shop:product_list")

def cart_detail(request):
    items, total = get_cart(request)

    return render(request, "shop/cart_detail.html", {
        "items": items,
        "total": total,
    })

@require_POST
def cart_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("shopping_cart", {})

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (ValueError, TypeError):
        return redirect("shop:cart_detail")

    if quantity <= 0:
        cart.pop(str(product.id), None)

    elif quantity <= product.stock and product.is_available:
        cart[str(product.id)] = quantity

    request.session["shopping_cart"] = cart

    return redirect("shop:cart_detail")


@require_POST
def cart_remove(request, product_id):
    cart = request.session.get("shopping_cart", {})

    cart.pop(str(product_id), None)

    request.session["shopping_cart"] = cart

    return redirect("shop:cart_detail")
