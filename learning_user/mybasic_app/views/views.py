from django.shortcuts import redirect, render

# hado lel login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout



from mybasic_app.models import ToDolist, Item
from mybasic_app.forms import createNotelist



from ..decorators import evaluteur_required


# hnaa ykon swlahe liiiiiiiiiiiiiiiiiiiiiiiiiiiii 
    # en relation donc mchi t3 eval w mchi t3 chrch exctement



def LoginByProfile(request):
    if request.user.is_authenticated:
        
        if request.user.is_evaluteur:
            return redirect('evaluteur:dashboardeval')

        if request.user.is_chercheur:
            return redirect('chercheur:dashboardchrch')

        if request.user.is_superuser:
            return redirect('/MakaniAdmin')

               
    else:
        return render(request, 'registration/login.html')






@login_required  # tema hadi zdena hata ida dekhel w dar login bch nkhdemo decarotors
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homme'))







@login_required
def createNote(response):
    if response.method == "POST":
        form = createNotelist(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDolist(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/myapp/mynote")

    else:
        form = createNotelist()

    return render(response, "account/createmynote.html", {"form": form})


def mynote(response):
    return render(response, "account/mynote.html", {})


def Merci(response):
    if response.method == "POST":
        return HttpResponse("<h1> Success !! </h1>")


def mylist(response, id):
    ls = ToDolist.objects.get(id=id)
    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    # createNote
                    ls.item_set.create(text=txt, complete=False)

                else:
                     return HttpResponse("<h1> invalide </h1> ")

        return render(response, "account/myliste.html", {"ls": ls})
    return render(response, "account/mynote.html", {})


