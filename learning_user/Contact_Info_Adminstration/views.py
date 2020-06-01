from django.shortcuts import render, redirect
from django.views import generic
from Contact_Info_Adminstration.models import Contact_MAKANI_CF,SearchQuery

from Contact_Info_Adminstration.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



from learning_user import settings

from django.contrib.auth.decorators import login_required



class PostList(generic.ListView):
    context_object_name= 'post_list'
    queryset = Contact_MAKANI_CF.objects.filter(status=1).order_by('-created_on')
    template_name = 'Contact/index.html'  # a list of all posts will be displayed on index.html
    model = Contact_MAKANI_CF



class PostDetail(generic.DetailView):
    model = Contact_MAKANI_CF
    template_name = 'Contact/post_detail.html'  # detail about each Contact  post will be on post_detail.html






@login_required
def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message Pour  Sujet De : {form.cleaned_data["Sujet"]}  , from email : {form.cleaned_data["email"]}'
            message = form.cleaned_data["Message_Detailles"]
            sender = form.cleaned_data['email']
            recipients = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message, [sender], [recipients], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'Contact/contact.html', {'form': form})



###########   2020-05-15 ##########"""
from Poste_By_Admin.models import BlogPost

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'searches/view.html',context)