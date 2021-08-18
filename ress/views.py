from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory # model form for querysets
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ContactForm
from .models import Contact
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
            print(form)
            form.save()
            messages.success(request,"This email has been sent")
            
    
    form= ContactForm()
    

    context = {
        "form": form
    }
    # trx= request.POST.get('acc')
    # print(trx)



    #     if request.htmx:
            

    #         return HttpResponse("Created",context)
    #         # context = {
    #         #     "object": obj
    #         # }
    #         # return render(request, "recipes/partials/detail.html", context)
    #     return HttpResponse("confirmed",context)
    if request.htmx:
        return render(request,"confirm.html",context)
    return render(request, 'home.html', context)
    

