from django.db import models


class Cart(models.Model):
    """

    Cart model for Market place.


    A Customer may have one or more Carts active
    at anyone time.  A Cart must be related to a
    Store; and for each Store, 'Checked Out' separately.

    The UI may facilitate a batch of Cart Checkouts, so
    the Customer experiences something that 'feels' like
    a single checkout process.

    The payment details are reused for each Checkout,
    at the Customer's discression.

    Checkout also depends on who is handling settlement
    of funds.  If CommonMarket place is the Agent, then
    it is possible to settle the one or more Carts in
    a single payment.  Otherwise it'll be a Checkout per
    Store
    """

    store = models.ForeignKey(
        'agents.Store')

class CartItem(models.Model):
    """
    A CartItem can accept any object that decends
    from the polymorphic class Product.
    """

    cart = models.ForeignKey(
        'Cart')

    # Expects polymorphic Resource > Product > Object
    product = models.ForeignKey(
        'products.Product')

    def product_class(self):
        return self.product.get_real_instance_class()
