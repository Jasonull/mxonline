from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.


def login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            auth_login(request, user)
            return render(request, "index.html")
    elif request.method == "GET":
        return render(request, "login.html", {})
