from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from Main.forms import UserLoginForm


def authorization(request):
    # return render(request, 'Main/authorization.html')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = auth.authenticate(email=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'Main/authorization.html', context)


def registration(request):
    return render(request, 'Main/registration.html')


def register(request):
    return render(request, 'Main/register.html')


def main(request):
    return render(request, 'Main/main.html')
