from django.shortcuts import get_object_or_404
from products.models import Product

# cart items will not be stored in db but in session, so items added to cart will be lost when user logs out

# method allowing anything added to cart to be available on display on any web page within the web app. Previously in 'all products' view, which could only take products was put into a dictionary in 'render', which is called a 'context' available to all pages across web app

# session stored entirely in browser memory


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
# initialising
    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        # will always know unique id
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        # key values pairs
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
