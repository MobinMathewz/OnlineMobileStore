from django.forms import ModelForm
from product.models import Brand, Mobile, Orders
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BrandCreateForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets ={
            'brand_name':forms.TextInput(attrs={'class':'form-control'})
        }


class MobileCreateForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'

        widgets = {
         "mobile_name":forms.TextInput(attrs={'class':'form-control'}),
         "ram":forms.TextInput(attrs={'class':'form-control'}),
         "price":forms.TextInput(attrs={'class':'form-control'}),
         "camera":forms.TextInput(attrs={'class':'form-control'}),
         "os":forms.TextInput(attrs={'class':'form-control'}),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"

        widgets={
            "personname": forms.TextInput(attrs={'readonly': 'readonly'}),
            "address": forms.TextInput(attrs={'readonly': 'readonly'}),
            "pin": forms.TextInput(attrs={'readonly': 'readonly'}),
            "phone": forms.TextInput(attrs={'readonly': 'readonly'}),
            "email": forms.TextInput(attrs={'readonly': 'readonly'}),
            "productid": forms.TextInput(attrs={'readonly': 'readonly'}),
            "status":forms.HiddenInput()
                 }


class OrderUpdateForm(ModelForm):
    class Meta:
        model = Orders
        fields= '__all__'

        widgets = {
            "personname":forms.TextInput(attrs={'readonly':'readonly'}),
            "address":forms.TextInput(attrs={'readonly':'readonly'}),
            "pin":forms.TextInput(attrs={'readonly':'readonly'}),
            "phone":forms.TextInput(attrs={'readonly':'readonly'}),
            "email":forms.TextInput(attrs={'readonly':'readonly'}),
            "productid":forms.TextInput(attrs={'readonly':'readonly'}),
            "user": forms.HiddenInput(),
        }


class SearchForm(forms.Form):
    Brand_name = forms.CharField(max_length=120)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"   ( it will display all fields which is unwanted for us.)
        fields = ["first_name","last_name","email","username","password1","password2"]