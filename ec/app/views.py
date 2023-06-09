from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Product
from django.db.models import Count
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Customer

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val) 
        # print("product is: ", product[0].__dict__)
        title = Product.objects.filter(category=product[0].category).values('title')
        print("Title is ", title)
        return render(request, 'app/category.html', locals())
    
class ProductDetail(View, ):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'app/productdetail.html', locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully...")
        else:
            messages.warning(request, "Invalid input data.")
        return render(request, 'app/customerregistration.html', locals())
    
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        user = request.user
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            cust = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, zipcode=zipcode, state=state)
            cust.save()
            messages.success(request, "Congratulations! Profile created successfully...")
        else:
            messages.warning(request, "Invalid input data.")
        return render(request, 'app/profile.html', locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())

class UpdateAddressView(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/update_address.html', locals())
        
    def post(self, request, pk):
        print(request.POST)
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add.user = request.user
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.state = form.cleaned_data['state']            
            add.save()
            messages.success(request, "Congratulations! Profile updated successfully...")
        else:
            messages.warning(request, "Invalid input data.")
        return redirect("address")
    
