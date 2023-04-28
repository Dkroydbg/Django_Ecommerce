from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.

def index(request):
    products=None
    categories=Category.get_all_categories()
    categoryId=request.GET.get('category')
    if categoryId:
        products=Product.get_all_product_by_categoryid(categoryId)
    else:
        products=Product.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'index.html',data)
    #return render(request,'order/orders.html')


def validateCustomer(customer):
    error_message=None
    if not customer.first_name:
        error_message="First name is required"
    elif len(customer.first_name)<4:
        error_message="First name must be at least 4 characters"
    elif not customer.last_name:
        error_message="Last name is required"
    elif len(customer.last_name)<4:
        error_message="Last name must be at least 4 characters"
    elif not customer.phone:
        error_message="Phone number is required"
    elif len(customer.phone)<10:
        error_message="Phone number must be at least 10 characters"
    elif len(customer.password)<6:
        error_message="Password must be at least 6 characters"
    elif len(customer.email)<6:
        error_message="Email must be at least 6 characters"
    elif customer.isExists():
        error_message="email already exists"
    return error_message


def registerUser(request):
    postData=request.POST
    first_name=postData.get('firstname')
    last_name=postData.get('lastname')
    phone=postData.get('number')
    email=postData.get('email')
    password=postData.get('password')
    #validation

    value={
        'first_name':first_name,
        'last_name':last_name,
        'phone':phone,
        'email':email,
    }
    error_message=None

    customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)

    error_message=validateCustomer(customer)
    

    

    #saving
    if not error_message:
        print(first_name,last_name,phone,email,password)
        customer.password=make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
        data={
            'error':error_message,
            'values':value
        }
        return render(request, 'signup.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        return registerUser(request)
    

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.objects.filter(email=email).first()
        error_message=None
        if customer and check_password(password,customer.password):
            return redirect('homepage')
        else:
            error_message="email or passsword invalid"
            return render(request,'login.html',{'error':error_message})
