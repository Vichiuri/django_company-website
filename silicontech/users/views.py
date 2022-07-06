from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from tally.users.forms import NewValuerForm, CustomerRelationForm
from tally.users.models import CustomerRelation

User = get_user_model()


@login_required(login_url=settings.LOGIN_URL)
def create_valuer(request):
    if request.method == "POST":
        form = NewValuerForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                name=form.cleaned_data['name'],
                national_id=form.cleaned_data['national_id'],
            )
            return redirect('users:valuers')
    else:
        form = NewValuerForm()
    context = {'form': form}
    return render(request, 'tally/users/create_valuer.html', context)


@login_required(login_url=settings.LOGIN_URL)
def list_valuers(request):
    superuser = User.objects.first()
    valuers = User.objects.exclude(id=superuser.pk)
    context = {'valuers': valuers}
    return render(request, 'tally/users/valuers.html', context)


def update_valuer(request, pk):
    valuer = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = NewValuerForm(request.POST, instance=valuer)
        if form.is_valid():
            form.save()
            return redirect('users:valuers')
    else:
        form = NewValuerForm(instance=valuer)
    context = {"form": form}
    return render(request, 'tally/users/create_valuer.html', context)


@login_required(login_url=settings.LOGIN_URL)
def delete_valuer(request, pk):
    valuer = get_object_or_404(User, pk=pk)
    valuer.delete()
    return redirect('users:valuers')






