from django import forms
from django.forms import inlineformset_factory
from .models import Product, Order, Stock, Textile, Color, Size, AdditionalImage, BoughtProduct

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):   
    pass  

class SignUpForm(UserCreationForm):   
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'password1', 'password2')

class BuyForm(forms.ModelForm):
    class Meta:
        model = BoughtProduct
        fields = ('__all__')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('color', 'size', 'order_quantity')    
    
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')    

    def clean_name(self):       
        name = self.cleaned_data['name']
        duplicate = Product.objects.filter(name = name).exists()        
        if duplicate:            
            raise forms.ValidationError('This articule was already used. Please try another.')
        return name

class AddImageForm(forms.ModelForm):    
    class Meta:
        model = AdditionalImage
        fields = ('additional_image',)                

class AddStockForm(forms.ModelForm):
    size_xs = forms.IntegerField(label='q-ty xs', initial=0)
    size_s = forms.IntegerField(label='q-ty s', initial=0)
    size_m = forms.IntegerField(label='q-ty m', initial=0)
    size_l = forms.IntegerField(label='q-ty l', initial=0)
    size_xl = forms.IntegerField(label='q-ty xl', initial=0)
    size_2xl = forms.IntegerField(label='q-ty 2xl', initial=0)
    size_3xl = forms.IntegerField(label='q-ty 3xl', initial=0)
    size_4xl = forms.IntegerField(label='q-ty 4xl', initial=0)

    class Meta:
        model = Stock
        fields = ('product', 'color')

class AddTextileForm(forms.ModelForm):
    class Meta:
        model = Textile
        fields = ('__all__')

class AddColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ('__all__')

class AddSizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ('__all__')

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'textile', 'image', 'description')
