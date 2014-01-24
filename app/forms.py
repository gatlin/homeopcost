#forms
from django import forms
from django.conf import settings

class LoginForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput(render_value=False))

class NewUserForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=200, widget=forms.EmailInput)
	email_again = forms.EmailField(max_length=200, widget=forms.EmailInput)
	password = forms.CharField(max_length=200, widget=forms.PasswordInput)
	password_again = forms.CharField(max_length=200, widget=forms.PasswordInput)


	def clean(self):
		cleaned_data = self.cleaned_data
		if(cleaned_data.get('password') != cleaned_data.get('password_again')):
			raise forms.ValidationError("The passwords entered do not match.")
		if(cleaned_data.get('email') != cleaned_data.get('email_again')):
			raise forms.ValidationError("The emails entered do not match.")
		return cleaned_data

class CardForm(forms.Form):
	cc = forms.CharField(max_length=16, widget=forms.NumberInput)
	csv = forms.CharField(max_length=3, widget=forms.NumberInput)

	def clean(self):
		cleaned_data = self.cleaned_data
		if len(cc) != 16:
			raise forms.ValidationError("CC incorrect")
		if len(csv) != 3:
			raise forms.ValidationError("CSV incorrect")
		if not name or not address or not city or not state or not zipcode:
			raise forms.ValidationError("Not all fields filled in.")
		return cleaned_data