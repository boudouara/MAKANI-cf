from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,DetailView
from ..decorators import chercheur_required
from ..forms import ChercheurSignUpForm,From_Edite_Profile,ArticleForm,ConfForm
from ..models import User,Chercheur ,Article,Topic,Conferance

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from django.forms import inlineformset_factory
from django.core.files.storage import FileSystemStorage




#+++++++++++++++++
from mybasic_app.filters import FilterClass





class ChercheurSignUpView(CreateView):
	model = User
	form_class = ChercheurSignUpForm
	template_name = 'registration/signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'chercheur'

		return super().get_context_data(**kwargs)


	def form_valid(self ,form):
		user = form.save()
		login(self.request, user)
		return redirect('chercheur:dashboardchrch') 





@login_required
@chercheur_required
def profil_chrch(request):
	return render(request, 'Templchercheur/profil_chrch.html')


@login_required
@chercheur_required
def ToContact(request):
	return render(request, 'Templchercheur/contactAS_chrcheur.html')



@login_required
@chercheur_required
def Userchrch(request):

	return render(request, 'Templchercheur/profile-page.html')


'''

@login_required
@chercheur_required
def AccedeauDoc_Aschrch(request):
	return render(request, 'Templchercheur/docs/documentation.html')
'''


#+++++++++++++++++++++++++++++++++++++++++++++     10/06/2020   +++++++++++++++++++++++++++++-

@login_required
@chercheur_required
def CreeArticle(request ):

	User = request.user
	formset = ArticleForm()   
	if request.method == 'POST':
		formset = ArticleForm(request.POST , request.FILES)
			   
		if formset.is_valid():
			 article = formset.save(commit=False)
			 article.date_posté
			 article.author = Chercheur.objects.get(user=User)
			 article.save()
			 return redirect('chercheur:tach_ARTCL')

	context = {'formset': formset }
	return render(request, 'Templchercheur/register-page.html' ,context)






@login_required
@chercheur_required
def Delete_list(request):
	User = request.user
	researcher = Chercheur.objects.get(user=User)
	articles = Article.objects.filter(author = researcher)
	myfilter=FilterClass(request.GET , queryset=articles)
	articles = myfilter.qs
	context = {'articles': articles ,'myfilter':myfilter}
	return render(request, 'Templchercheur/Delete_List_Article.html' , context)






@login_required
@chercheur_required
def Delete(request , pk):
	User = request.user
	researcher = Chercheur.objects.get(user=User)
	article = Article.objects.filter(author = researcher).get(pk = pk)
	article.delete()
	return redirect('chercheur:list_delete_Article')




@login_required
@chercheur_required
def Update_detaille_list(request):
	User = request.user 
	researcher = Chercheur.objects.get(user=User)
	articles = Article.objects.filter(author = researcher) ##++++++++++++++ chkon li dar hada aartcile
   ############              #######      ##########
	#chrch = chercheur.objects.all()
	myfilter=FilterClass(request.GET , queryset=articles)
	articles = myfilter.qs
	context = {'articles': articles ,'myfilter':myfilter}
	
	return render(request, 'Templchercheur/les_articl_Detailles.html' , context)




@login_required
@chercheur_required
def Update(request ,pk ):

	User = request.user
	researcher = Chercheur.objects.get(user=User) ##+++++++++++++++  chkon li dar hada aartcile
	article = Article.objects.filter(author = User.id ).get(pk = pk)
	formset = ArticleForm(instance = article)
	
	if request.method == 'POST':
		formset = ArticleForm(request.POST , request.FILES  ,instance = article)
   
		if formset.is_valid():
			 article = formset.save(commit=False)
			 article.date_posté
			 article.author = Chercheur.objects.get(user=User)
			 article.Conferance.name = formset.cleaned_data['Conferance']
			 article.save()
			 return redirect('chercheur:tach_ARTCL')

	context = {'formset': formset}
	return render(request, 'Templchercheur/modifèè.html' ,context)






####################
@method_decorator([login_required, chercheur_required], name='dispatch')
class Edit_Myprofil(UpdateView):
	template_name = 'Templchercheur/edite_myprofil.html'
	model = User
	form_class = From_Edite_Profile

	def get_success_url(self):
		return reverse_lazy('chercheur:Profile')
	 


'''
hadi khaliha aprr nsthe9aha f filter apree  !!!! 

	def get_queryset(self):
		qs = self.model.objects.all()
		list_td = FilterClass_prfl(self.request.GET, queryset=qs)
		return list_td.qs
'''


@login_required
@chercheur_required
def AccedeauDoc_Aschrch(request):
	User = request.user
	chrch = Chercheur.objects.get(user=User) 
	articles = Article.objects.filter(author = chrch )
	context = {'articles': articles}
	return render(request, 'Templchercheur/docs/documentation.html',context)



# +++++++++++++++++++++++++++++++++++ 2020/05/15   +++++++++++++++++++++++++++++
  
@login_required
@chercheur_required
def confList(request, pk):
    topic = Topic.objects.get(id = pk)
    conferances= Conferance.objects.filter(topic = topic)
    conf_count = conferances.count()
    context = {'topic':topic, 'conferances':conferances, 'conf_count':conf_count}

    return render(request, 'Templchercheur/All_Confernce.html', context)





@method_decorator([login_required, chercheur_required], name='dispatch')
class topicList(ListView):
   template_name = 'Templchercheur/All_Topics.html'
   model = Topic        
   paginate_by = 5

   def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['number'] = Topic.objects.all().count()
    return context   




@method_decorator([login_required, chercheur_required], name='dispatch')
class ConfDetailView(DetailView):
    template_name = 'Templchercheur/Conf_Detailles.html'
    model = Conferance
    form_class = ConfForm



