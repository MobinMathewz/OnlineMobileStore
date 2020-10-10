from django.shortcuts import render,redirect
from product.forms import BrandCreateForm, MobileCreateForm,OrderForm,OrderUpdateForm,SearchForm,RegistrationForm
from product.models import Brand,Mobile,Orders

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def createBrand(request):
    form = BrandCreateForm()
    context={}
    context["form"] = form
    qs = Brand.objects.all()
    context["brands"] = qs
    if request.method=="POST":
        form = BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("brandcreate")

    return render(request,"product/createBrand.html",context)


def brandEdit(request,pk):
    obj = Brand.objects.get(id=pk)
    form = BrandCreateForm(instance=obj)
    context={}
    context['form']=form
    if request.method=="POST":
        obj = Brand.objects.get(id=pk)
        form = BrandCreateForm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("brandcreate")
    return render(request,'product/brandedit.html',context)

def brandDelete(request,pk):
    obj = Brand.objects.get(id=pk)
    form = BrandCreateForm(instance=obj)
    context = {}
    context['form'] = form
    if request.method=="POST":
        obj = Brand.objects.filter(id=pk).delete()
        return redirect("brandcreate")
    return render(request,'product/branddelete.html',context)

def createMobile(request):
    form = MobileCreateForm()
    context ={}
    context["form"] = form
    mobiles =Mobile.objects.all()
    context["mobiles"] = mobiles
    if request.method=="POST":
        form = MobileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("mobilecreate")
    return render(request,"product/createMobile.html",context)

def mobileEdit(request,pk):
    obj = Mobile.objects.get(id=pk)
    form = MobileCreateForm(instance=obj)
    context = {}
    context["form"] = form
    if request.method=="POST":
        obj = Mobile.objects.get(id=pk)
        form = MobileCreateForm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobilecreate')
    return render(request,"product/mobileedit.html",context)


def mobileView(request,pk):
    obj = Mobile.objects.get(id=pk)
    context = {}
    context["mobile"] = obj
    return render(request,"product/itemview.html",context)

def mobileDelete(request,pk):
    obj = Mobile.objects.get(id=pk)
    form = MobileCreateForm(instance=obj)
    context = {}
    context["form"] = form
    if request.method=="POST":
        obj = Mobile.objects.filter(id=pk).delete()
        return redirect("mobilecreate")
    return render(request,"product/deletemobile.html",context)



@login_required(login_url='loginPage')
def index(request):
    mobiles = Mobile.objects.all()
    context = {}
    context["mobiles"] = mobiles
    form = SearchForm()
    context["search"] = form
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data.get("Brand_name")
            products = Mobile.objects.filter(brand__brand_name=brand) #brand is ForiegnKey which refers to 'Brand' model where 'brand_name' is there. So use 'brand__brand_name'
            context["mobiles"] = products
            return render(request,"product/index.html",context)
    return render(request,"product/index.html",context)


@login_required(login_url='loginPage')
def order(request,pk):
    form = OrderForm(initial={"productid":pk, "user":request.user})
    context = {}
    context["form"] = form
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            context["form"]=form
            return render(request,'product/success.html',context)
    return render(request,"product/purchase.html",context)


def viewOrders(request):
    qs = Orders.objects.filter(user=request.user,active_status=1)
    context = {}
    context["qs"] = qs
    return render(request,"product/adminViewOrders.html",context)

def orderDetails(request,pk):
    qs = Orders.objects.get(id=pk)
    product = qs.productid
    item = Mobile.objects.get(id=product)
    form = OrderUpdateForm(instance=qs)
    context = {}
    context["form"] = form
    context["item"] = item
    if request.method=="POST":
        form = OrderForm(instance=qs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewoders")
    return render(request,"product/orderdetails.html",context)

def register(request):
    form = RegistrationForm()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
    return render(request,'product/registration.html',context)

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username,",",password)
        if ((username=="admin")&(password=="admin")):
            return render(request,"product/adminbase.html")
        user = authenticate(request,username=username,password=password)
        if user is not None:   #if authentication not fails
            login(request,user)
            return redirect("index")
        else:
            return redirect("loginPage")
    return render(request,"product/login.html")


def logOutPage(request):
    logout(request)
    return redirect('loginPage')