from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
# Create your views here.
@login_required
def feed(req):

    categories_to_filter = ['bags']

    category_filters = Q()
    for category in categories_to_filter:
        category_filters |= Q(category__contains=category)

    classic = Product.objects.filter(category_filters)[:6]

    product = Product.objects.all().filter(Availability=True)[:8]
    product_4 = Product.objects.all().filter(Availability=True)[:4]
    male = Product.objects.filter(name__icontains="male").filter(Availability=True)[:6]
    both = Product.objects.filter(name__icontains="female").filter(Availability=True)[:6]
    newest_products = Product.objects.all().order_by('-created_at').filter(Availability=True)[:6]
    context = { "product": product, 
                "4_product": product_4, 
                "newest_products": newest_products,
                "male": male,
                "both": both,
                "classic": classic
                }
    return render(req, "ecommerce/index.html", context)


@login_required
def cart(req):
    customer = req.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    print(items)
    num_items = items.count()
    total_sum = sum(item.product.price * item.quantity for item in items)
    context = { "item": items,
                "num_items": num_items, 
                "total": total_sum
                }
    return render(req, "ecommerce/shoping-cart.html", context)

@login_required
def checkout(req):
    customer = req.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    num_items = items.count()
    total_sum = sum(item.product.price * item.quantity for item in items)
    context = {"item": items, "num_items": num_items, "total": total_sum}
    return render(req, "ecommerce/checkout.html", context)

def update_item(request):
        data = json.loads(request.body.decode("utf-8"))  # Parse the JSON data from the request body
        product_id = data.get("productID")
        action = data.get("action")
        customer = request.user

        # Get the product and order
        product = Product.objects.get(id=product_id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        # Update the quantity based on the action
        if action == "add":
            order_item.quantity += 1
        elif action == "remove":
            order_item.quantity -= 1

        # Save the order item
        order_item.save()

        # If quantity is zero or less, delete the order item
        if order_item.quantity <= 0:
            order_item.delete()

        return JsonResponse({"message": "Item updated successfully"}, status=200)
def productDetail(req, id):

    product = Product.objects.get(id=id)
    categories_to_filter = list(product.category)

    category_filters = Q()
    for category in categories_to_filter:
        category_filters |= Q(category__contains=category)

    classic = Product.objects.filter(category_filters)[:5]
    clas = Product.objects.filter(category_filters)[:4]
    context = {
        "product": product,
        "classic": classic,
        "clas": clas
    }
    return render(req, "ecommerce/shop-details.html", context)



@login_required
def shop_listing(req):
    categories_to_filter = ['bags']

    category_filters = Q()
    for category in categories_to_filter:
        category_filters |= Q(category__contains=category)

    classic = Product.objects.filter(category_filters)[:6]
    max_bag = Product.objects.filter(category_filters)[:20]
    product_4 = Product.objects.all().filter(Availability=True)[:4]
    context = {
        'product': product_4,
        'bags': classic,
        'bag': max_bag
    }
    return render(req, 'ecommerce/shop-grid.html', context)

@login_required
def bag_listing(req):
    categories_to_filter = ['bags']

    category_filters = Q()
    for category in categories_to_filter:
        category_filters |= Q(category__contains=category)

    classic = Product.objects.filter(category_filters)[:6]
    max_bag = Product.objects.filter(category_filters)[:20]
    product_4 = Product.objects.all().filter(category_filters)[:4]
    context = {
        'product': product_4,
        'bags': classic,
        'bag': max_bag
    }
    return render(req, 'ecommerce/shop-grid.html', context)

@login_required
def shoes_listing(req):
    categories_to_filter = [
                            'Shoes',
                            "Athletic Shoes",
                            'Casual Shoes',
                            'Formal Shoes',
                            'Boots',
                            'Sandals'
                            'Flip-Flops',
                            'Loafers',
                            'Slip-Ons',
                            'Sneakers',
                            'Brogues',
                            'Running Shoes', 
                            'Ballet Flats', 
                            ]

    category_filters = Q()
    for category in categories_to_filter:
        category_filters |= Q(category__contains=category)

    classic = Product.objects.filter(category_filters)[:6]
    max_bag = Product.objects.filter(category_filters)[:20]
    product_4 = Product.objects.all().filter(category_filters)[:4]
    context = {
        'product': product_4,
        'bags': classic,
        'bag': max_bag
    }
    return render(req, 'ecommerce/shop-grid.html', context)