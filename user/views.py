from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        # is_valid() metodu forms.py dosyasında tanımladığımız clean metodunu çağırır
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User()
        newUser.username = username
        newUser.set_password(password)
        newUser.save()

        messages.success(request, "Başarıyla kayıt oldunuz...")

        return redirect("index")
    if form.errors:
        messages.info(request, "Bir hata meydana geldi.")
    context = {
        "form": form
    }
    return render(request, "register.html", context)
    # if request.method == "POST":
    #     # Post = create - update
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         # is_valid() metodu forms.py dosyasında tanımladığımız clean metodunu çağırır
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #
    #         newUser = User()
    #         newUser.username = username
    #         newUser.set_password(password)
    #         newUser.save()
    #
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "register.html", context)
    # else:
    #     # get request olursa boş form göndermeliyiz
    #     form = RegisterForm()
    #     context = {
    #         "form": form,
    #         "isim": "selçuk",
    #         "soyad": "akarın"
    #     }
    #     return render(request, "register.html", context)


def my_login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        # biz authenticate metoduyla veritabanımızdaki user'ımıza ulaşmış oluruz
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola yanlış.")
            return render(request, "login.html", context)
        login(request, user)
        messages.success(request, "Başarıyla giriş yaptınız.")
        return redirect("index")

    return render(request, "login.html", context)


def my_logout(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız.")
    return redirect("index")
