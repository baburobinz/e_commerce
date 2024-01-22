from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def show_cart(request):
    user = request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context ={
        'cart':cart_obj,
    }
    return render(request,'cart.html',context)

@login_required(login_url='account')
def add_cart_item(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        quantity = int(request.POST.get('quantity'))
        cart_obj,created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        ordered_item,created = OrderedItem.objects.get_or_create(
            product = product,
            owner=cart_obj
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()       
        else:
            ordered_item.quantity+=quantity
            ordered_item.save()
    return redirect('cart')

def remove_from_cart(request,pk):
    item = OrderedItem.objects.get(pk=pk)
    item.delete()
    return redirect('cart')


def confirm_order(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        total_price = float(request.POST.get('total_price'))
        try:
            order = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )

            if order:
                order.order_status=order.ORDER_CONFIRMED
                order.total_price=total_price
                order.save()
                show_message = 'Your Order has been processed'
                messages.success(request,show_message)

        except Exception as e:
                show_message = 'No items found..!'
                messages.error(request,show_message)
        

    return redirect('cart')
        
       
@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context = {'orders':all_orders}
    return render(request,'orders.html',context)

