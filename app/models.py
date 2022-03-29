from datetime import datetime
from distutils.command.upload import upload
from email import message
from django.db import models
# for signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.
STATUS = (('active','active'),('','default'))

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS,blank=True,max_length=200)
    image = models.ImageField(upload_to = "Product_Image/Slider_Image")
    price_image = models.ImageField(upload_to = "Product_Image/Slider_Image")

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=200)
    data_toggle = models.CharField(max_length=150,null=True,blank=True)
    icon = models.CharField(max_length=100,null=True,blank=True)
    type = models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.name

class SmallCategories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.name
        
class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Price(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE = {
        ('1000 TO 10000', '1000 TO 10000'),
        ('10000 TO 20000', '10000 TO 20000'),
        ('20000 TO 30000', '20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000'),
    }
    price = models.CharField(choices=FILTER_PRICE,max_length=68)

    def __str__(self):
        return  self.price

from django.utils import timezone
class Product(models.Model):
    STOCK = ('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK')
    STATUS = ('Publish','Publish'),('Draft','Draft')

    unique_id = models.CharField(unique=True,max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to ="Product_Image/product")
    created_date = models.DateTimeField(default=timezone.now)
    stock = models.CharField(choices=STOCK,max_length=200,null=True,blank=True)
    status = models.CharField(choices=STATUS,max_length=200,null=True,blank=True)
    

    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)
    subcategories = models.ForeignKey(SubCategories,on_delete=models.CASCADE,blank=True,null=True)
    smallcategories = models.ForeignKey(SmallCategories,on_delete=models.CASCADE,blank=True,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name


# class UsercreateForm(UserCreationForm):
#     email = forms.EmailField(required=True,label='Email',error_messages='This email is already exists')

    # class Meta:
    #     model = User
    #     fields = ('username','email','password1','password2')

    # def save(self, commit=True):
    #     user = super(UserCreationForm,self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user

    # def clean_email(self):
    #     if User.objects.filter(email = self.cleaned_data['email']).exists():
    #         raise forms.ValidationError(self.fields['email'].error_message['exists'])
        # return self.cleaned_data['email']


class Order(models.Model):
    image = models.ImageField(upload_to = "Product_Image/order")
    product = models.CharField(max_length=1000,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.CharField(max_length=5)
    total = models.CharField(max_length=1000,default='')
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.today)
    # date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.product


# blog list
class Blog_list(models.Model):
    title = models.CharField(max_length=255)
    editor = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to = "Product_Image/blog")
    description = models.TextField()

    def __str__(self):
        return self.title

 







































