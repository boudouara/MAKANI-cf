from django.urls import path,include
from .views import chercheur,evaluteur,views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
     path('login/',views.LoginByProfile, name="LoginByProfile"),

    


###################""


  path('myapp/chercheur/', include(([
  	  path('', chercheur.profil_chrch, name='dashboardchrch'),
      path('contact',chercheur.ToContact , name='Contact_chrch_ou_admin'),
      path('myprofile_AsChercheur',chercheur.Userchrch,name='Profile'),
      path('CréaArticle',chercheur.CreeArticle,name='CreeArticle'),
      path('DeleteARTCL',chercheur.Delete_list,name='list_delete_Article'),
      path('UpdateARTCL',chercheur.Update_detaille_list,name='tach_ARTCL'),
      path('Documentation_chrh/',chercheur.AccedeauDoc_Aschrch,name='AccedeauDoc_Aschrch'),
      path('EditeProfile/<str:pk>/',chercheur.Edit_Myprofil.as_view(),name='EditeProfile'),
              # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   10/05/2020     ++++++++++++++++++++++++++++++++++
  
      path('DeleteARTCL/<str:pk>/',chercheur.Delete,name='Delate'),
      path('UpdateArTCL/<str:pk>/',chercheur.Update,name='Update'),
              # +++++++++++++++++++++++++++++++++++++++++++++   15/05/2020     ++++++++++++++++++++++++++++++++++
      path('conf_list/<str:pk>/',chercheur.confList,name='conf_list'),
      path('conf_detaille/<str:pk>/',chercheur.ConfDetailView.as_view(),name='conf_detaille'),
      path('topic_list/',chercheur.topicList.as_view(),name='topic_list'),



    

                                     ], 'views'), namespace='chercheur')),





    path('myapp/evaluteur/', include(([

       path('', evaluteur.profil_eval , name='dashboardeval'), # hadi engenrale
       path('contact',evaluteur.ToContact , name='Contact_eval_ou_admin'),
       path('myprofileAsEvaluateur/',evaluteur.Usereval,name='Profile'),  # hadi sepecile lel user
       path('Articles/',evaluteur.Liste_All_Artcl.as_view(), name='listeArtcile'),
       path('Confrences/',evaluteur.Liste_All_Confrence.as_view() , name='All_Confernce'),
       path('Liste/',evaluteur.all_list , name='listeNv'),# z3ma ga3 les them wla confrence
       path('Evalution/',evaluteur.evaluéé , name='evaluéé'),
       path('Documentation_evl',evaluteur.AccedeauDoc,name='AccedeauDoc'),
       path('EditeProfile/<str:pk>/',evaluteur.Edit_Myprofil_As_Eval.as_view(),name='EditeProfileAs_eval'),
       path('etat_chrch/',evaluteur.All_Etat_Du_Cherchr.as_view() , name='Etat_All_Chrch'),


       path('Allcommite/',evaluteur.All_Commite.as_view() , name='AllCommite'),
       #path('Votrecommite/',evaluteur.Mon_Commite.as_view() , name='MonCommite'),





                                      ], 'views'), namespace='evaluteur')),





###############" hado swalhe persssonel t3 kol user bch ytfkre wla ki agendaa "

    path('create/',views.createNote, name="create"),
    path('mynote/',views.mynote, name="mynote"),
    path('merci/',views.Merci, name="merci"),


  


    
        ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)