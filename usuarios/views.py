from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        primeiro_nome = request.POST.get("primeiro_nome")
        ultimo_nome = request.POST.get("ultimo_nome")
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não são iguais.")
            return redirect("/usuarios/cadastro")

        if len(senha) < 6:
            messages.add_message(
                request, constants.ERROR, "A senha deve ter no mínimo 6 caracteres."
            )
            return redirect("/usuarios/cadastro")

        try:
            if not username == User.username:
                user = User.objects.create_user(
                    first_name=primeiro_nome,
                    last_name=ultimo_nome,
                    username=username,
                    email=email,
                    password=senha,
                )
        except:
            messages.add_message(request, constants.ERROR, "Usuário já existe.")
            return redirect("/usuarios/cadastro")
        
        messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso.")
        return redirect("/usuarios/cadastro")


def logar(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos.")        
            return redirect("/usuarios/login")