from django.shortcuts import render
from mybasic_app.models import User

from mybasic_app.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



@login_required
@staff_member_required
def En_choisi(request):
	 
	 #if User.is_evaluteur :
	 return render(request,'Pour_Evaluaéé/mth_evluéé.html')




#>>>>>>>>>>>    hadi il rani dayreha haka structure   

def Liste_choisi(request):
	 
	 return render(request,'Pour_Evaluaéé/Voir_liste_choisi.html')


