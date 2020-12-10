from django.forms import ModelForm 
from .models import Order


#Make sure that you import this inside the views.py
# this is how you take care of forms
class OrderForm(ModelForm):
     class Meta:
         model = Order  # Order is the table Order
         fields = '__all__' #  <-  go ahed and create form with all of this fields in it
         # just for one field or 2 we can us
         # fields = ['customer', product]