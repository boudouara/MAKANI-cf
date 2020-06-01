from django.shortcuts import render


def Homme(request):
    return render(request,'homme.html')




def Aboute__Us(request):
    return render(request,'Abouteus.html')



###########################  
from Poste_By_Admin.models import BlogPost


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# hadi tleme gaaaaaaaaaaaaaaaaaaaaa3 les poste ki chrch ki eval ki admin 
# hna aya wahde yji ychofe ki inscre ki mchi inscree  
def Poste_page(request):
    qs = BlogPost.objects.all()
    context = {"title": "From Makani-CF-", 'blog_list': qs}
    return render(request, "Poste_by_Admin/home.html", context)

