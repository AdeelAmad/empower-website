from django.shortcuts import render
from empower.models import homePage, contactPage, event, image
from django.views.generic import ListView
# Create your views here.

def index(request):
    context = { "what": homePage.objects.get(id=1).whatwedo,
                "mission": homePage.objects.get(id=1).mission }
    return render(request, 'index.html', context=context)

def contact(request):
    context = {}
    context['contacts'] = []
    for o in contactPage.objects.all():
        context['contacts'].append(o.contactinfo)

    print(context)

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
    return render(request, 'shop.html')