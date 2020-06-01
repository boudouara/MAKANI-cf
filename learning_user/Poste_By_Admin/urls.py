from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
    blog_post_create_view,
)

urlpatterns = [
    path('', blog_post_list_view,name='My_List_Blog'), # hadi t3 kol wahde ychofo swalhehehe
    path('new/', blog_post_create_view,name='Create_Newblog'),
    path('<str:slug>/', blog_post_detail_view,name='Detail_Blog'),
    path('<str:slug>/edit/', blog_post_update_view,name='Update_Blog'),
    path('<str:slug>/delete/', blog_post_delete_view,name='Delete_Blog'),
]

