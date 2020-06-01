from django.urls import path
from . import views
from .views import (evalList, EvalCreateView, EvalUpdateView, EvalDeleteView,
    cherList, CherCreateView, CherDeleteView, CherUpdateView, HomePageView

,confList,ConfUpdateView,ConfCreateView,
ConfDeleteView,ConfDetailView,ArticlList_Conf, Confmodifier

,ComiteCreateView, ComiteUpdateView
    )



urlpatterns = [
    
    # les liste li3ndnaaaaaaaaaaaaaaaaaaaa ga3 f jiha t3na admin 
    path('',HomePageView.as_view(),name ="dashboard"),
    path('gest_eval/', evalList.as_view(), name="ges_eval"),
    path('gest_cher', cherList.as_view(), name="ges_cher"),
     path('gest_conf/', confList.as_view(), name="ges_conf"),




#++++++++++++++++++++++ admin men jihete chandiire lel  eval
    path('evalEdit/<str:pk>/', EvalUpdateView.as_view(), name="editEval"),
    path('evalCreate/', EvalCreateView.as_view(), name="createEval"),
    path('<pk>/deleteEval/', EvalDeleteView.as_view(), name="deleteEval"), 
  

#++++++++++++++++++++++++++ admin men jihete chandiire lel  chrchr
    
    path('editCher/<str:pk>/', CherUpdateView.as_view(), name="editCher"),
    path('createCher/', CherCreateView.as_view(), name="createCher"),
    path('<pk>/deleteCher/', CherDeleteView.as_view(), name="deleteCher"),
   

         

    # hadi kante aapliaction smoha Gconf ms ni hatiteh f account bch ndiro 
    #app wahde lel adminnstration  w kate dyera des prblm  ni riglthoom rahi f chbebe
    
    #++++++++++++++++++++++++++ admin men jihete chandiire lel  cConfrencess

   
    path('confEdit/<str:pk>/', ConfUpdateView.as_view(), name="confEdit"),
    path('confCreate/', ConfCreateView.as_view(), name="confCreate"),
    path('<pk>/deleteConf/', ConfDeleteView.as_view(), name="deleteConf"), 
    path('confDetail/<str:pk>/', ConfDetailView.as_view(), name="confDetail"),
    path('modifier/<str:pk>/', Confmodifier.as_view(), name="modifier"),
    
    
    
# +++++++ 2020/05/15 +++++++++
    path('article_conf/<str:pk>/',ArticlList_Conf,name='article_conf'),
    path('comiteCreate',ComiteCreateView.as_view(),name='comiteCreate'),
    path('comiteEdit/<str:pk>/', ComiteUpdateView.as_view(), name="comiteEdit"),
    
  



    
]


    
