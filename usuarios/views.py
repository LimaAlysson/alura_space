from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['username'].value()
            password = form['password'].value()
        
        user = auth.authenticate(
            request,
            username=name,
            password=password,
        )
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["password_1"].value() != form["password_2"].value():
                return redirect('cadastro')

            name = form["signup_name"].value()
            email = form["email"].value()
            password = form["password_1"].value()

            if User.objects.filter(username=name).exists():
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password,
            )
            user.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})