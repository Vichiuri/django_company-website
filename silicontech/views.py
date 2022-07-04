from django.shortcuts import render
from silicontech.models import Contact
from django.contrib import messages


def project_index(request):

    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def services(request):

    return render(request, 'services.html')


def portfolio(request):

    return render(request, 'portfolio.html')


def team(request):

    return render(request, 'team.html')


def contact(request): 
    
     if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject =request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject =subject
        contact.message = message
        contact.save()
        
        messages.success(request, 'Your message has been sent. Thank you!')
     return render(request, 'contact.html') 
 
    
