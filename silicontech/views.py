from django.shortcuts import render
from silicontech.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms
from django.shortcuts import redirect, render


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
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        messages.success(request, 'Your message has been sent. Thank you!')
    return render(request, 'contact.html')


@login_required()
def home(request):
    silicontech = Contact.objects.all()
    context = {
        'silicontech': silicontech
    }

    return render(request, 'home.html', context)
