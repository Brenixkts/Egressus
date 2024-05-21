from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'egressusapp/index.html')

def renderizar_login_page(request):
    return render(request, 'egressusapp/login.html')