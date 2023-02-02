from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser


@login_required
def form_view(request):
    if request.method == 'POST':
        # Save the form data to the database
        CustomUser.objects.create(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number']
        )
        # Clear the form and show a success message
        return render(request, 'form.html', {'message': 'Data saved successfully!'})
    return render(request, 'form.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('form_view')
        else:
            return render(request, 'login.html', {'error': 'Invalid Login Credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('form_view')
