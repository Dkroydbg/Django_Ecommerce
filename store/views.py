from django.shortcuts import render
from django.http import HttpResponse
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

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('number')
        email=postData.get('email')
        password=postData.get('password')
        print(first_name,last_name,phone,email,password)
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        customer.register()

        return HttpResponse("Recieved post request")
