from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import evaluteur_required
from ..forms import  EvaluteurSignUpForm,From_Edite_Profile
from ..models import  User,Evaluateur,Article,Conferance,Commite

from django.http import HttpResponseRedirect, HttpResponse




class EvaluteurSignUpView(CreateView):
    model = User
    form_class = EvaluteurSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'evaluteur'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #if Evaluteur.Code_Eval =="makani" :
        user = form.save()
        login(self.request, user)
        return redirect('evaluteur:dashboardeval')         # hadi dashboard en genralle ga33
        #else :
            #return HttpResponseRedirect(reverse('homme'))






@login_required
@evaluteur_required
def profil_eval(request):
	return render(request,'Templevaluteur/Dachboardeval.html')




@login_required
@evaluteur_required
def ToContact(request):
    return render(request,'Templevaluteur/contactAs_evaluteur.html')




@login_required
@evaluteur_required
def Usereval(request):
    return render(request,'Templevaluteur/ProfileEval.html')






@login_required
@evaluteur_required
def all_list(request):
    return render(request,'Templevaluteur/List_Artcl_Evaluee.html')


@login_required
@evaluteur_required
def evaluéé(request):
    return render(request,'Templevaluteur/evaluation.html')


@login_required
@evaluteur_required
def AccedeauDoc(request):
    return render(request,'Templevaluteur/docs/documentation.html')




####################
@method_decorator([login_required, evaluteur_required], name='dispatch')
class Edit_Myprofil_As_Eval(UpdateView):
    template_name = 'Templevaluteur/Eval_edite_myprofile.html'
    model = User
    form_class = From_Edite_Profile
    
    def get_success_url(self):
        return reverse_lazy('evaluteur:Profile')
     



#+++++++++++++++++++++++++++++++++++++
@method_decorator([login_required, evaluteur_required], name='dispatch')
class Liste_All_Artcl(ListView):
    model = Article
    template_name = 'Templevaluteur/All_Artcles.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbrArctl'] = Article.objects.all().count()
        return context




@method_decorator([login_required, evaluteur_required], name='dispatch')
class Liste_All_Confrence(ListView):
    model = Conferance
    template_name = 'Templevaluteur/All_Conf.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbrConf'] = Conferance.objects.all().count()
        return context        



@method_decorator([login_required, evaluteur_required], name='dispatch')
class All_Etat_Du_Cherchr(ListView):
    model = User
    template_name = 'Templevaluteur/All_chercheur.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbrchrch'] = User.objects.filter(is_chercheur=True).count()
        return context        




@method_decorator([login_required, evaluteur_required], name='dispatch')
class All_Commite(ListView):
    model = Commite
    template_name = 'Templevaluteur/All_Commite.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbrCommite'] = Commite.objects.all().count()
        return context        
