from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem, account_number
from .forms import OrderCreateForm

def order_create(request):
    cart = Cart(request)
    account= account_number.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form, 'account': account})

