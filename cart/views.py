from django.shortcuts import render
from .models import Product, User
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
def index(request):
    products = Product.objects.all()
    params = {'product': products}
    if request.method == "POST":
        p_name = request.POST.get('name')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        p = int(price)
        q = int(qty)
        tot_price = p*q

    return render(request, 'index.html', params)


def user(request):
    confirm = request.POST.get('confirm', 'off')
    if request.method == "POST":
        if confirm == "on":
            f_name = request.POST.get('f_name', '')
            l_name = request.POST.get('l_name', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            add1 = request.POST.get('add1', '')
            add2 = request.POST.get('add2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            code = request.POST.get('code', '')

            user = User(f_name=f_name, l_name=l_name, email=email, password=password, add1=add1, add2=add2, city=city, state=state, code=code)
            user.save()
            messages.success(request, 'You are successfully Signed In...')
        else:
            messages.warning(request, 'Please confirm your details...')

    return render(request, 'user.html')


def my_cart(request):

    return render(request, 'cart.html')


def search(request):
    query = request.GET.get('search')
    if query:
        result = Product.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )
        params = {'product': result}
    else:
        return HttpResponse("<h1><center>Please Search anything</center></h1>")

    return render(request, 'search.html', params)
