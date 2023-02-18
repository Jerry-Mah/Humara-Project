from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        print("hello")
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = User.objects.get(username = email)
                
            except:
                # messages.error(request, "Username does not exist")
                print("Not found")
            user = authenticate(request, username =email, password= password )
            if user is not None:
                login(request, user)
                # messages.error(request, "Successfully loged in")
                return redirect('home')
            else:
                # messages.error(request, "Username or password is incorrect")
                pass

    return render(request, 'authentication/login.html' )