import imp
from django.shortcuts import render, redirect
from .models import *
#Usermodel
from django.contrib.auth.models import User
from django.contrib import messages
# for signup
from django.contrib.auth import authenticate,login,logout
#addtocart
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



# Create your views here.

def base2(request):
    return render(request,'Main/base2.html')

def base(request):
    categories = Categories.objects.all()
    smallcategories= SmallCategories.objects.all()
    subcategories = SubCategories.objects.all()
    brand = Brand.objects.all()
    filter_price = Filter_Price.objects.all()

    context = {
        "categories":categories,
        "smallcategories":smallcategories,
        "subcategories":subcategories,
        "brand":brand,
        "filter_price":filter_price,
    }

    return render(request,'Main/base.html',context)

def index(request):
    slider = Slider.objects.all()
    categories = Categories.objects.all()
    smallcategories= SmallCategories.objects.all()
    subcategories = SubCategories.objects.all()
    filter_price = Filter_Price.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.all()
   
    context = {
        "slider": slider,
        "categories":categories,
        "smallcategories":smallcategories,
        "subcategories":subcategories,
        "filter_price":filter_price,
        "brand":brand,
        "product":product,
    }

    return render(request,'Main/index.html',context)


def product(request):
    product = Product.objects.filter(status = 'Publish')
    categories = Categories.objects.all()
    smallcategories= SmallCategories.objects.all()
    subcategories = SubCategories.objects.all()
    filter_price = Filter_Price.objects.all()
    brand = Brand.objects.all()
 
    CATID = request.GET.get('categories')
    SUBCAT_ID = request.GET.get('subcategories')
    SMALLCAT_ID = request.GET.get('smallcategories')
    BRAND_ID = request.GET.get('brand')
    PRICE_FILTER_ID = request.GET.get('filter_price')

    if CATID:
        product = Product.objects.filter(categories = CATID)
    elif SUBCAT_ID:
        product = Product.objects.filter(subcategories = SUBCAT_ID)
    elif SMALLCAT_ID:
        product = Product.objects.filter(smallcategories = SMALLCAT_ID)
    elif BRAND_ID:
        product = Product.objects.filter(brand = BRAND_ID)
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(filter_price=PRICE_FILTER_ID)
    else:
        product = Product.objects.filter(status = 'Publish').order_by('-id')

     
    context = {
        "product":product,
        "categories":categories,
        "smallcategories":smallcategories,
        "subcategories":subcategories,
        "filter_price":filter_price,
        "brand":brand,
        
    }

    return render(request,"Main/product.html",context)


def product_detail(request,id):
    categories = Categories.objects.all()
    smallcategories= SmallCategories.objects.all()
    subcategories = SubCategories.objects.all()
    brand = Brand.objects.all()
    filter_price = Filter_Price.objects.all()
    product = Product.objects.filter(id=id).first()


    context = {
        "categories":categories,
        "smallcategories":smallcategories,
        "subcategories":subcategories,
        "brand":brand,
        "filter_price":filter_price,
        "product":product,
    }


    return render(request,"Main/product_detail.html",context)



def search(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains = query)

    context = {
        'product':product
    }

    return render(request,'Main/search.html',context)

# from django.db.models import Q
# def search(request):
#     query = request.GET.get('query')
#     product = Product.objects.filter(Q(name__icontains=query) | Q(categories__icontains=query))

#     context = {
#         'product':product
#     }

#     return render(request,'main/search.html',context)


 
from django.core.mail import EmailMessage 
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,

        )
        data.save()

        email = EmailMessage(
            'Hello',
            'Hello thanks for the messaging us. We will get follw back to you!',
            'a074b9c2c123cf',
            [email],
        )
        email.send()
        return redirect('index')
 
    return render(request,'main/contact.html')

 
def register(request):
	# if request.method == "POST":
	# 	username = request.POST.get['username']
	# 	email = request.POST.get['email']
	# 	password = request.POST.get['password']
	 
	# 	if User.objects.filter(username = username).exists():
	# 		messages.error(request,"The username is already usded.")
	# 		return redirect('register')

	# 	elif User.objects.filter(email = email).exists():
	# 		messages.error(request,"The email is already used.")
	# 		return redirect('register')

	# 	else:
	# 		user = User.objects.create_user(
	# 		    username = username,
	# 			email = email,
	# 			password = password
	# 			)
	# 		user.save()
	# 		return redirect('index')

	return render(request,'registration/auth.html')

 
# from django.contrib.auth import authenticate,login, logout


def signup(request):
    return render(request,'registration/signup.html')



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def checkout(request):
    if request.method =="POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)

      
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b



            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total,
            )
            order.save()
        request.session['cart'] = {}

        return redirect('index')
    return render(request,"cart/checkout.html")



def your_order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid) 

    order = Order.objects.filter(user = user)

    context = {
        'order':order,
    }

    return render(request,'order.html',context)


def blog(request):
    categories = Categories.objects.all()
    smallcategories= SmallCategories.objects.all()
    subcategories = SubCategories.objects.all()
    filter_price = Filter_Price.objects.all()
    brand = Brand.objects.all()
    blog = Blog_list.objects.all()
   
    context = { 
        "categories":categories,
        "smallcategories":smallcategories,
        "subcategories":subcategories,
        "filter_price":filter_price,
        "brand":brand,
        "blog":blog,
    }

    return render(request,'Main/blog.html',context)


















 








 

