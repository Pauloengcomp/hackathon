from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirecionar para a página inicial após o login
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    
    return render(request, 'login.html')




def dashboard_view(request):
    return render(request, 'dashboard.html')