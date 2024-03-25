from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password','class':'form-control'}))

  class Meta:
    model = Account
    fields=['first_name','last_name','phone_number','email','password']

  def clean(self):
      cleaned_data=super(RegistrationForm,self).clean()
      password=cleaned_data.get('password')
      confirm_password=cleaned_data.get('confirm_password')

      if password != confirm_password:
        raise forms.ValidationError("password does not match!")
      return cleaned_data 

  def __init__(self,*args,**kwargs):
    super(RegistrationForm,self).__init__(*args,**kwargs)
    self.fields['first_name'].widget.attrs['placeholder']='Enter first name'
    self.fields['last_name'].widget.attrs['placeholder']='Enter last name'
    self.fields['phone_number'].widget.attrs['placeholder']='Enter phone_number'
    self.fields['email'].widget.attrs['placeholder']='Enter email address'
    for field in self.fields:
      self.fields[field].widget.attrs['class']='form-control'


    

