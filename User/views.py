from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from .models import posts

def Home(request):
    return render(request, 'Home.html')

@login_required
def post(request):
    if request.method=='POST':
        post_text = request.POST['my_text']
        created = request.POST['created']
        updated = request.POST['updated']
        new_post = posts(text=post_text,created_at=created,updated_at=updated)
        new_post.user = request.user
        new_post.save()
        return render(request, 'post.html')
    else:
        return render(request, 'post.html')


def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'email taken')
                 return redirect('signup')
            else:      
                usr = User.objects.create_user(username=username,password=password2,first_name=first_name,last_name=last_name,email=email)
                usr.save()
                messages.info(request, 'user saved')   
                return redirect('login')           
        else:
            messages.info(request, 'password not matching')
            return redirect('signup')
        
        

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['Password']

        usr = auth.authenticate(username=username,password=password)

        if usr is not None: 
            auth.login(request, usr)
            return redirect('post')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('Home')

