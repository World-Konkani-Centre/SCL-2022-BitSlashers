from decimal import Context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login,logout,models
import http.client
from .models import Product
# @login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'index.html')

def about(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'about.html')

def contact(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'contact.html')

def trend(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'pricetrend.html')

def user_analytics(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'user_analytics.html')

def option(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'option.html')

def view_store(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'view_store.html')

def sample(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'sample-inner-page.html')

def service(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'services.html')

def service_detail(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'service-details.html')

def sell(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
       product = request.POST['product']
       quantity = request.POST['quantity']
       price = request.POST['price']
       phone = request.POST['phone']
       country = request.POST['Country']
       state = request.POST['State']
       district = request.POST['District']
       pin_code = request.POST['pin-code']
       ins = Product(product_name=product, product_quantity=quantity, product_price=price, phone_number=phone, seller_country=country, seller_state=state, seller_district=district, pin_code=pin_code)
       ins.save()
    return render(request, 'sell.html')

def buy(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'buy.html')

def confirm(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'confirm.html')

def buyer(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'buyer.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'profile.html')



def loginp(request):
    if request.method=="POST":
        mobile = request.POST.get('mobile')
        conn = http.client.HTTPSConnection("kptries-otp-api.herokuapp.com")
        payload = 'number='+str(mobile)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/send", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        request.session['mobile']=mobile
        return redirect("/otp/")
    return render(request, 'login.html')

def signup(request):
    # is_auth=request.session['auth']
    # if is_auth is not "true":
        # return redirect("/login/")
    if request.method=="POST":
        mobile = request.session['mobile']
        pincode=request.POST.get('pincode')
        name=request.POST.get('name')
        city=request.POST.get('city')
        role=request.POST.get('role')
        userId="user"+str(Profile.objects.all().count()+1)
        user = User(username = userId,first_name=name)
        user.save()
        profile = Profile(user = user , mobile=mobile , pincode=pincode,role=role,city=city) 
        profile.save()
        login(request,user)
        return redirect("/home/")
    return render(request, 'signup.html')

def otp(request):
    if request.method=="POST":
        mobile = request.session['mobile']
        otp=request.POST.get('OTP')
        conn = http.client.HTTPSConnection("kptries-otp-api.herokuapp.com")
        payload = 'number='+str(mobile)+'&otp='+str(otp)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/verify", payload, headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        if data.find("Success")!=-1:
            profile = Profile.objects.filter(mobile = mobile).first()
            if not profile:
                # request.session['auth']="true"
                return redirect("/signup/")
            login(request,profile.user)
            return redirect("/home/")
        else:
            return redirect("/invalid")
    return render(request,'otp.html')


def invalid(request):
    return render(request,'invalid.html')

def my_logout(request):
    logout(request)
    return redirect('login')