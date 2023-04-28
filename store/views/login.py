from django.views import View
from ..models.customer import Customer
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password


class Login(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.objects.filter(email=email).first()
        error_message=None
        if customer and check_password(password,customer.password):
            request.session['customer_id'] = customer.id
            request.session['email'] = customer.email
            return redirect('homepage')
        else:
            error_message="email or passsword invalid"
            return render(request,'login.html',{'error':error_message})