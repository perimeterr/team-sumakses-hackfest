from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import SignUpForm, SignInForm

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'sign_up.html', {'sign_up_form': sign_up_form})
    else:
        sign_up_form = SignUpForm()
    return render(request, 'sign_up.html', {'sign_up_form': sign_up_form})

def sign_in(request):
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data['username']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                sign_in_form.add_error(None, "Invalid username or password")
        return render(request, 'sign_in.html', {'sign_in_form': sign_in_form})
    else:
        sign_in_form = SignInForm()
    return render(request, 'sign_in.html', {'sign_in_form': sign_in_form})

def home(request):
    return render(request, 'home.html')

def sign_out(request):
    logout(request)
    return redirect('/signIn')