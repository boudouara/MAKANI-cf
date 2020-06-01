from django import forms
from mybasic_app.models import ToDolist
from django.core import validators



from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from mybasic_app.models import (Chercheur, User ,Evaluateur,Article , Conferance , Article)
from django.forms.utils import ValidationError



'''
def check_for_z(value):
    if value[0].lower() != '' :
        raise forms.ValidationError("NAME MUST BE STARTS BY  Z ")

'''



class EvaluteurSignUpForm(UserCreationForm):
    
    email = forms.EmailField(error_messages={'exists': 'This already exists!'})
    verify_email=forms.EmailField()
    Code_Eval = forms.CharField(max_length=30)
    

    ## kyn li rani mkhlihom w kyn li suppp
    ## li khlithom li9 ykono bch verifee wla rahom sepicei
    ### li mhithom pcq deja kynin model  donc 
    ## be   class >> UserCreationForm  y3rfhom

    class Meta(UserCreationForm.Meta):
  
        model = User
        fields=('first_name','last_name','username','password1','password2',
            'email','verify_email','Code_Eval','Organization','Country','site_Personnel',
            'City','Post_code','Address_line_principale','Address_line','Phone',
            'profile_pict',)

     

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if User.objects.filter(email=email).exists():
            raise ValidationError(" No !!!  ,  Email exists")


        if vmail != email :
            raise forms.ValidationError(" CHECK Your :  EMIAL !!! ")
        


    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile_pict = self.cleaned_data.get('profile_pict')
        user.is_evaluteur = True
        if commit:
            user.save()
            evaluteur=Evaluateur.objects.create(user=user)
            evaluteur.email=self.cleaned_data.get('email')
            evaluteur.Code_Eval=self.cleaned_data.get('Code_Eval')

            evaluteur.save()
        return user








###############













class ChercheurSignUpForm(UserCreationForm):
 
    email = forms.EmailField()
    verify_email=forms.EmailField(required=True)   
    Info_personel =forms.CharField(required=False)


    class Meta(UserCreationForm.Meta):
        model = User
        fields=('first_name','last_name','username','password1','password2',
            'email','verify_email','site_Personnel','Organization','Country','Phone',
            'City','Post_code','Address_line_principale','Address_line',
            'profile_pict','Info_personel')

     
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if User.objects.filter(email=email).exists():
            raise ValidationError(" No !!!  ,  Email exists")

        if vmail != email :
            raise forms.ValidationError(" CHECK Your :  EMIAL ! ")
        


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.profile_pict = self.cleaned_data.get('profile_pict')
        user.is_chercheur = True          #juste pour save extnde kima ngilo f User"
        user.save()
        chercheur = Chercheur.objects.create(user=user)
        chercheur.email=self.cleaned_data.get('email')     #Juste bch save the personel 3ndek "


        chercheur.save()
        
        return user





class createNotelist(forms.ModelForm):
    
    class Meta():
        model = ToDolist
        fields = ('name',)


# +++++++++++++++++++++++++++++++  10/05/2020 ++++++++++++++++++++++++++++++++++++++++ 


class From_Edite_Profile(forms.ModelForm):
    
    Info_personel =forms.CharField(required=False)

    class Meta():
        model=User
        fields=('first_name','last_name','username','email',
        'site_Personnel','Organization','Country','Phone',
        'City','Post_code','Address_line_principale','Address_line',
            'profile_pict','Info_personel')





class ArticleForm(forms.ModelForm):

    name = forms.CharField(label='Article name ..',
                           widget=forms.TextInput(attrs={'placeholder': ' Article name'}))

    class Meta:
        model = Article
        fields = ['name' , 'description', 'Conferance','document']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }




class ConfForm(forms.ModelForm):
    class Meta:
        model = Conferance
        fields = '__all__'
