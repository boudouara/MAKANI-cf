from . import views
from django.urls import path


app_name = 'Contact_Info_Adminstration'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('contact/', views.contact_form, name='contact'),
   
  
]