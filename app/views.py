
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from app.models import Product, ContactMessage, Subscriber, History
from django.contrib import messages

# Create your views here.


@login_required
def home(request):
    user = request.user
    my_products = Product.objects.filter(owner=user).order_by('-created_at')
    market_place = Product.objects.all().exclude(owner=user).order_by('-craeted_at')
    context ={
        'my_products': my_products,
        'market_place': market_place,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        message= request.POST.get('message')
        if not name or not email or not message:
            messages.error (request,'All field required')
            return redirect(reverse('home'))
        new_contact = ContactMessage.objects.create(
            name=name, email=email, message=message
        )
        new_contact.save()
        messages.success(request,'Message recieved successfully')
    return render(request, 'contact.html')


def subscribe(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email :
            messages.error(request, 'All field required')
            return redirect(reverse('home'))
        allready_sub = Subscriber.objects.filter(email=email).exists()
        if allready_sub:
            messages.error (request, 'You have allready subscribed')
            return redirect (reverse('home'))
        email_is_incorrect = Subscriber.objects.filter(email=email).exists()
        if email_is_incorrect:
            messages.error(request, 'The email is incorret')
        new_sub = Subscriber.objects.craete(
            email=email,
        )
        new_sub.save()
        messages.success(request, 'Thank for subscribing')
        return redirect (reverse('home'))
        return redirect (reverse('home'))
        
        
def history(request):
    user = request.user
    record = History.objects.filter(user=user)
    context ={
        "History": record
    }
    return render(request, 'History.html', context)