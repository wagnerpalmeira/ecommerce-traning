from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login


def criar_cliente(request):
    if request.method == 'GET':
        return render(request, 'criar_cliente.html')
    elif request.method == 'POST':
        user = get_user_model()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user_created = user.objects.create(
            email=email
        )

        user_created.set_password(senha)
        user_created.save()

        return redirect('/')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username=email, password=senha)
        print(user)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('produtos:listar_produtos'))