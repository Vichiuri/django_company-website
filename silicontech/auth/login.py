from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):
    if request.method == "POST":

        print("Post")
        print(request.POST)
        user = authenticate(name=request.POST['name'], national_id=request.POST['national_id'],
                            password=request.POST['password'])

        if user is not None:
            print(user)
            auth_login(request, user)
            messages.success(request, f"Login Successful, welcome {user.name}")
            return redirect(settings.LOGIN_REDIRECT_URL)

        else:
            return redirect(settings.LOGIN_URL)

    return render(request, 'silicontech/users/login.html')
