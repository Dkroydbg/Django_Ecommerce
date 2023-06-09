from django.views import View
from ..models.customer import Customer
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
# from store.middleware.auth import auth_middleware


class OrderView(View):
    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_order_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})
    
