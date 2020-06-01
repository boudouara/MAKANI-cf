from django.contrib import admin
from django.urls import path,include
from . import views as viewsPj
from mybasic_app.views import chercheur, evaluteur,views
from django.conf import settings



#####################
from Contact_Info_Adminstration.views import search_view




urlpatterns = [
    path('1salah2toufik3ahmed4islam5nadjet6nariman789/', admin.site.urls), #hadaa path tree essencieles attention
    path('',viewsPj.Homme,name='homme'),
    path('AbouteUs',viewsPj.Aboute__Us,name='Aboute__Us'),



    path('myapp/',include('mybasic_app.urls')),
    path('logout/',views.user_logout,name="logout"),
     path('contact/', include('Contact_Info_Adminstration.urls')),



######
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/chercheur/', chercheur.ChercheurSignUpView.as_view() , name='chercheur_signup'),
    path('accounts/signup/evaluteur/', evaluteur.EvaluteurSignUpView.as_view(), name='evaluteur_signup'),

################## note perssonel
    path('<int:id>',views.mylist, name="mylist"),


#++++++++++++++++++++++++++++++++++++++++++++++++++++#partie adminstration 
path('MakaniAdmin/', include('accounts.urls'),name='MakaniAdmin'),

#############  2020/05/15   ########"
    path('Info-Poste', viewsPj.Poste_page,name='Info_Poste'),
    path('blog/', include('Poste_By_Admin.urls')),
    path('search/', search_view,name='searching'),




############      2020 / 05 / 18 ################""""

    path('G__evaluation/', include('G__evaluation.urls')),






]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



