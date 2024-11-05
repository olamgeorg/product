from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import auth, User
# Create your views here.


def signup(request):
    if request.method=='POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if not name or not lastname or not username or not email or not password or not cpassword:
            messages.error(request,'All field are required')
            return redirect(reverse('signup'))
        username_already_taken = User.objects.filter(username=username).exists()
        if username_already_taken:
            messages.error(request, 'The username is already taken')
            return redirect(reverse('signup'))
        if password != (cpassword):
            messages.error(request,'The password is not match')
            return redirect(reverse('signup'))
        if len (password) < 6:
            messages.error(request,'The password is not strong')
        email_already_taken = User.objects.filter(email=email).exists()
        if email_already_taken:
            messages.error(request,'The email is taken')
            return redirect(reverse('signup'))
        new_user = User.objects.create(
            name=name,
            lastname=lastname,
            username=username,
            email=email,
            password=password,
            cpassword=cpassword,
            owner = User,
        )
        new_user.save()
        messages.success(request, 'You have signup successfully')
        return redirect ( reverse('home'))
    return render( request, 'signup.html' )



def login(request):
    next = request.POST.get('next')
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request,'All field required')
            return redirect(reverse('login'))
        user = auth.authenticate(
            username=username,
            password=password,
            )
        if not user:
            messages.error(request, 'Invalid credential')
            return redirect(reverse('signup'))
        auth.login(request,user)
        return redirect(next or reverse ('home'))
    return render(request,'login.html' )


def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))


