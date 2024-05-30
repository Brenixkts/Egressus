from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'egressus_app/index.html')

def login_authentication(request):
    # Caso o método seja GET, é enviado a página login.html
    if request.method == "GET":
        return render(request, 'egressus_app/login.html')
    else:
        # Caso o método seja POST, recebe os dados do formulário em login.html
        email = request.POST.get('email')
        password = request.POST.get('password')
        #Autentica usuário
        user = authenticate(username=email, password=password)
        # Verifica se o usuário existe e se está como ativo
        if user is not None and user.is_active == True:
            #Realiza login do usuário
            login(request, user)
            return HttpResponse(f"Bem vindo {user.first_name}")
        else:
            # Caso o usuário não cumpra os requisitos ele retorna um erro de login
            return HttpResponse("Erro de login")
            

@login_required
def home(request):
    pass