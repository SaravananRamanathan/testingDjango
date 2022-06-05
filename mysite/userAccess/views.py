from django.shortcuts import redirect, render
from .forms import RegisterForm
    
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            print("register form is valid")
            return redirect("/");
    else:
        form=RegisterForm()
    return render(response,"userAccess/register.html",{"form":form})