from django.forms import ModelForm
from django import forms


from mybasic_app.models import Evaluateur, Chercheur,User,Conferance, Commite


class EvalForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'


################## hnaa khasenha tmodifa apree pcq kyn 
#### les feildes rahom ybano ziyadaa  
##  hadi ___all___  aprr nspiicifoo hnaa
######## pcq kon tchofo ki tkhyre dok f template jayne tfecha  


class CherForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'




class ConfForm(ModelForm):
	class Meta:
		model = Conferance
		fields = '__all__'




class ComiteForm(ModelForm):
	class Meta:
		model = Commite
		fields = '__all__'