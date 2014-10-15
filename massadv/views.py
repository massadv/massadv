from django.shortcuts import render
from massadv.models import Categories, Items, Cat, Users, Images
import random

def index(request):
    return render(request, "index.html", {})

def top(request):
    return render(request, "top.html", {})

def left(request):
    # For when we have some items...
    #categoryIds = Cat.objects.all().distinct() 
    #categories = Categories.objects.filter(id__in=categoryIds)
    categories = Categories.objects.all()
    return render(request, "left.html", {'categories': categories})

def main(request):
    
    count = Items.objects.filter(featured=True, sold=False, expired=False).count();
    
    if count <= 0:
        return render(request, "main.html", {})
    
    # Pick the rnum'th item from the featured items in our table
    item = Items.objects.filter(featured=True, sold=False, expired=False)[random.randint(0, count-1)];
    user = Users.objects,filter(id=item.user)
    images = Images.objects.filter(item_id=item['id'])
    categoryIds = Cat.objects.filter(item_id=item['id']) 
    categories = Categories.objects.filter(id__in=categoryIds)
    catStr = ",".join(categories)
    
    # Alter the description
    item['description'] = item['description'].replace('\n', '<br />')
    item['description'] = (item['description'][:200] + '..') if len(item['description']) > 75 else item['description']
    
    return render(request, "main.html", {'item': item,
                                         'user': user,
                                         'categories': catStr,
                                         'images': images
                                        })

def buy(request):
    return render(request, "buy.html", {})

def sell(request):
    return render(request, "sell.html", {})

def contact(request):
    return render(request, "contact.html", {})

def images(request):
    return render(request, "images.html", {})

def items(request):
    return render(request, "items.html", {})

def category(request, catid):
    return render(request, "category.html", {})

def details(request):
    return render(request, "details.html", {})

def register(request):
    return render(request, "register.html", {})

def manage(request):
    return render(request, "manage.html", {})

def settings(request):
    return render(request, "settings.html", {})
