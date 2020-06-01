from django.urls import path
from G__evaluation import views





urlpatterns = [
    path('ListeFinal',views.Liste_choisi,name='ListeFinal'),
    path('',views.En_choisi,name='enChoix'),

    	]