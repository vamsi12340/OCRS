from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from CrimeReportingSystem.models import MyProfile,ComplaintBox,contact



class UserRegistrationForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"enter email",
			"required":True,
			}),

		}   

class MyProfileForm(forms.ModelForm):
	class Meta:
		model = MyProfile
		fields = ["age","gender"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select Your Gender",
			}),
		}

class UserupdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid",
			}),
		}

class ChangepassForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"enter old password"
		}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"enter New password"
		}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"enter confirmation password"
		}))

	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']


class ComplaintForm(forms.ModelForm):
	class Meta:
		model=ComplaintBox
		fields="__all__"

class ContactForm(forms.ModelForm):
	class Meta:
		model=contact
		fields = ["Name","email","Description"]
		widgets = {
		"Name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"enter email",
			}),
		"Description":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter Description"
			}),
		}

