from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):

	#senha = forms.CharField(max_length=32, widget=forms.PasswordInput)
	#senha = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Usuario
		#widget = {'senha':PasswordInput(),}
		fields = ('nome','email','senha','habilitado')
		widget={'senha':forms.PasswordInput()}

		


