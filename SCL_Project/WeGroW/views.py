from decimal import Context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login,logout,models
import http.client
from .models import Product
from .distance_calc.distance import PincodeDistance
from .models import Contact_us
from .models import Sold,Bought,ForSale

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
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = Contact_us(name=name,phone=phone,subject=subject,message=message)
        ins.save()
        return redirect('/home/')
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
       cur_profile=Profile.objects.filter(user=request.user).first()
       phone = request.POST['phone']
       country = request.POST['Country']
       state = request.POST['State']
       district = request.POST['District']
       pin_code = request.POST['pin-code']
       prodId="prod"+str(Product.objects.all().count()+1)
       ins = Product(profile=cur_profile,prodId=prodId,product_name=product, product_quantity=quantity, product_price=price, phone_number=phone, seller_country=country, seller_state=state, seller_district=district, pin_code=pin_code)
       ins.save()
       forSale = ForSale(profile=cur_profile,prodId=prodId,product_name=product, product_quantity=quantity, product_price=price, phone_number=phone, seller_country=country, seller_state=state, seller_district=district, pin_code=pin_code)
       forSale.save()
       message=f"Congratulations! Your offer has been placed, let's hope to connect you to a buyer! Happy Trading :).\nThe details of the offer are :\nProduct Id: {prodId}\nProduct Name: {product}\n Product Quantity: {quantity} Quintal \n Product Price: Rs. {price} per Quintal"
       conn = http.client.HTTPSConnection("kptries-otp-api.herokuapp.com")
       payload = 'phone='+str(cur_profile.mobile)+'&message='+message
       headers = {
       'Content-Type': 'application/x-www-form-urlencoded'
       }
       conn.request("POST", "/message", payload, headers)
       res = conn.getresponse()
       return redirect("/option/")
    return render(request, 'sell.html')

def buy(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        name=request.POST['product']
        pincode=request.POST['pincode']
        p=PincodeDistance()
        products=Product.objects.filter(product_name=name)
        dist=[]
        for product in products:
            dis=p.getDistance(pincode,product.pin_code)
            while 1:
                if dist.count(dis) > 0:
                    dis+=1
                else:
                    break
            dist.append(dis)
        sorted_prod= [x for _,x in sorted(zip(dist,products))]
        context = {
        'products': sorted_prod,
        }
        return render(request,"view_store.html",context)
    return render(request, 'buy.html')

def confirm(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return redirect("/confirm/")
    print(request.user)

def confirmBuy(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'GET':
        prodId=request.GET['product']
        product=Product.objects.get(prodId=prodId)
        forSale=ForSale.objects.get(prodId=prodId)
        cur_profile=Profile.objects.filter(user=request.user).first()
        buyer = Bought(profile=cur_profile,seller_name=product.profile.user.first_name,prodId=product.prodId,product_name=product.product_name, product_quantity=product.product_quantity, product_price=product.product_price, phone_number=product.phone_number, seller_country=product.seller_country, seller_state=product.seller_state, seller_district=product.seller_district, pin_code=product.pin_code)
        buyer.save()
        seller = Sold(profile=product.profile,buyer_name=cur_profile.user.first_name,buyer_phone=cur_profile.mobile,prodId=product.prodId,product_name=product.product_name, product_quantity=product.product_quantity, product_price=product.product_price, phone_number=product.phone_number, seller_country=product.seller_country, seller_state=product.seller_state, seller_district=product.seller_district, pin_code=product.pin_code)
        seller.save()
        product.product_name=product.product_name+" Sold"
        product.save()
        forSale.delete()
        message=f"Congratulations! Your order has been placed, Please connect to your seller! Happy Trading :).\nThe details of the farmer are \nFarmer Name: {product.profile.user.first_name}\n  Farmer Phone Number: {product.profile.mobile}\nProduct Id: {product.prodId}\nProduct Name: {product.product_name}\n Product Quantity: {product.product_quantity} Quintal\n Product Price: Rs. {product.product_price} per Quintal"
        conn = http.client.HTTPSConnection("kptries-otp-api.herokuapp.com")
        payload = 'phone='+str(cur_profile.mobile)+'&message='+message
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/message", payload, headers)
        res = conn.getresponse()
        message=f"Congratulations! We see a buyer for your crop! Please connect to your Buyer! Happy Trading :).\nThe details of the Buyer are \nBuyer Name: {cur_profile.user.first_name}\n  Buyer Phone Number: {cur_profile.mobile}\nProduct Id: {product.prodId}\nProduct Name: {product.product_name}\n Product Quantity: {product.product_quantity} Quintal\n Product Price: Rs. {product.product_price} per Quintal"
        payload = 'phone='+str(product.profile.mobile)+'&message='+message
        conn.request("POST", "/message", payload, headers)
        res = conn.getresponse()
    return redirect("/home/")
    

def buyer(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'buyer.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method=="POST":
        mobile = request.POST.get('mobile')
        pincode=request.POST.get('pincode')
        name=request.POST.get('name')
        city=request.POST.get('city')
        user = request.user
        profile = Profile.objects.get(user = user)
        user.first_name=name
        profile.mobile=mobile
        profile.pincode=pincode
        profile.user.first_name=name
        profile.city=city
        user.save()
        profile.save()
        login(request,user)
    profile=Profile.objects.filter(user=request.user).first()
    context = {
        'profile': profile,
        }
    return render(request, 'profile.html',context)



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

def analyticsBought(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    profile=Profile.objects.filter(user=request.user).first()
    products=Bought.objects.filter(profile=profile)
    context = {
        'products': products,
        }
    return render(request, 'analytics_buyer.html',context)


def analyticsSold(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    profile=Profile.objects.filter(user=request.user).first()
    products=Sold.objects.filter(profile=profile)
    context = {
        'products': products,
        }
    return render(request, 'analytics_seller.html',context)


def analyticsForSale(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    profile=Profile.objects.filter(user=request.user).first()
    products=ForSale.objects.filter(profile=profile)
    context = {
        'products': products,
        }
    return render(request, 'analytics_forSale.html',context)

def analyticsOption(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'analytics_option.html')