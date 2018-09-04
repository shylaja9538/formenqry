from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from sub_project import forms
from .forms import UserRegistrationForm
#from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import user_info
from .models import File
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def home_page(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def form_rets(request):
    show=user_info.objects.all()
    my_dict={"insert":show}
    return render(request,'retrieve.html',context=my_dict)
def showfile(request):

    lastfile= File.objects.last()

    filepath= lastfile

    #filename= lastfile.name

    form= forms.FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()


        context= {'filepath': filepath,
        'form': form,

        }


    return render(request,'files.html',context={'form':form})




@login_required
def special(request):
        # Remember to also set login url in settings.py!
        # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
        # Log out the user.
    logout(request)
        # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
                registered = True
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})

#def form_log(request):
    #return render(request,'login.html',{})
def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect('index')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})
def form_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)

        else:
            print("fill with exact value")
    return render(request,'forms.html',{'form':form})
@login_required
def find_search(request):
    return render(request,'search.html',{})
@login_required
def searchview(request):
    if request.method=='POST':
        search_query=request.POST['search_box']
        if search_query:
            match=user_info.objects.filter(Q(Name__iexact=search_query) | Q(Email__iexact=search_query))
            if match:
                return render(request,'search.html',{"sr":match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/Fsearch/')
    return render(request,'search.html')
