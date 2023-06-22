from django.shortcuts import render, redirect
from empower.models import homePage, contactPage, event, image, product
from django.contrib import messages
import stripe

stripe.api_key = 'sk_test_51NLc4lKpCU5NhQdKl2ogZdZ9q9tkscap9pYbo4K62fT9wXgOq03HzG28tzvLKkFXGt9f1AyAo34XX6k81tZg27Pj00yTAVeNfA'


def index(request):
    context = {"what": homePage.objects.get(id=1).whatwedo,
               "mission": homePage.objects.get(id=1).mission,
               "banner": homePage.objects.get(id=1).banner,
               "bannerColor": homePage.objects.get(id=1).bannerColor,
               "bannerSize": homePage.objects.get(id=1).bannerSize}

    return render(request, 'index.html', context=context)


def contact(request):
    context = {}
    context['contacts'] = []
    for o in contactPage.objects.all():
        context['contacts'].append(o.contactinfo)

    return render(request, 'contact.html', context=context)


def gallery(request):
    context = {}
    context['images'] = []

    for o in image.objects.all():
        context['images'].append(o)

    return render(request, 'gallery.html', context=context)


def events(request):
    context = {}
    context['past'] = []
    context['upcoming'] = []
    for o in event.objects.filter(upcoming=False):
        context['past'].append(o)

    for o in event.objects.filter(upcoming=True):
        context['upcoming'].append(o)

    return render(request, 'events.html', context=context)


def shop(request):
    context = {}
    context['products'] = []

    if request.session.keys().__contains__('cart') == False:
        request.session['cart'] = []

    for o in product.objects.all():
        context['products'].append(o)

    return render(request, 'shop.html', context=context)


def cart(request):
    context = {}
    context['items'] = []
    if request.session.keys().__contains__('cart') == False:
        request.session['cart'] = []

    if request.session['cart'] == []:
        context['empty'] = True
    else:
        for o in request.session['cart']:
            try:
                context['items'].append(product.objects.get(stripeid=o))
            except:
                pass

    return render(request, 'cart.html', context=context)


def add_cart(request):
    if request.session.keys().__contains__('cart') == False:
        request.session['cart'] = []

    if request.method == 'GET':
        request.session['cart'].append(request.GET.get('item'))
        request.session.modified = True

    messages.success(request, 'Item added to cart')
    return redirect('shop')


def remove_cart(request):
    if request.session.keys().__contains__('cart') == False:
        request.session['cart'] = []

    if request.method == 'GET':
        request.session['cart'].remove(request.GET.get('item'))
        request.session.modified = True

    messages.success(request, 'Item removed from cart')
    return redirect('cart')


def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        shipping_address_collection={"allowed_countries": ["US"]},
        shipping_options=[
            {
                "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 7, "currency": "usd"},
                    "display_name": "Standard Shipping",
                    "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 5},
                        "maximum": {"unit": "business_day", "value": 7},
                    },
                }
            }
        ],
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1NLsuxKpCU5NhQdKa0U1vwXI',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://testbed2.agradehost.com/shop/success',
        cancel_url='https://testbed2.agradehost.com/shop/cart',
    )

    return redirect(checkout_session.url, code=303)

def success(request):
    request.session['cart'] = []
    request.session.modified = True
    return render(request, 'success.html')

def aboutus(request):
    return render(request, 'aboutus.html')
