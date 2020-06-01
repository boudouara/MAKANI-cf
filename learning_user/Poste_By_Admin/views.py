from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from Poste_By_Admin.forms import BlogPostModelForm
from Poste_By_Admin.models import BlogPost





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++  hnaayaaa  3ndek tcree w sayii bsehe ki 
#tkon adminn tnjme tcree w tsuprimee w update 



@login_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
        return redirect("/blog")
    template_name = 'Poste_by_Admin/form.html'
    context = {'form': form}
    return render(request, template_name, context)  



#  ++++++++++++++++++++++++++++++++++++++++++++++  kol wahde w swalhehe
def blog_post_list_view(request):
                            # list t3 blogpost +  search
                            # queryset -> list of python object
    qs = BlogPost.objects.all().published() 
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 




def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)   




@login_required
@staff_member_required 
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/blog")
    template_name = 'Poste_by_Admin/form.html'
    context = {"title": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)  




@login_required
@staff_member_required 
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)  









