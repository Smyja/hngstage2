from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory # model form for querysets
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ContactForm
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail



def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        usernayme = request.POST.get('email')

        if form.is_valid(): 
            print(form)
            form.save()
            subject = 'This email is a test email for the hng backend task'
            message = f'Hello {usernayme}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [usernayme]
            send_mail( subject, message, email_from, recipient_list )

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
    

