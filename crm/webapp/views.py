from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddClientForm, UpdateClientForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Client
from django.contrib import messages



# Homepage
def home(request):
    return render(request, 'webapp/index.html')



# Register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('mylogin')
        elif not form.is_valid():
            messages.error(request, "Invalid Username/Password!")
            return redirect("register")

    context = {'register_form': form}

    return render(request, 'webapp/register.html', context=context)


# Login a user
def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)
            
            messages.success(request, "Logged in!")

            return redirect("dashboard")
        
        elif not form.is_valid():
            messages.error(request, "Username/Password Incorrect!")
            return redirect("mylogin")

    context = {'login_form': form}

    return render(request, 'webapp/mylogin.html', context=context)


# Dashboard
@login_required(login_url='mylogin')
def dashboard(request):
  
    my_clients = Client.objects.all()

    context = {'clients': my_clients}

    return render(request, 'webapp/dashboard.html', context=context)


# Add a client
@login_required(login_url='mylogin')
def add_client(request):
    form = AddClientForm()

    if request.method == "POST":
        form = AddClientForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Client Added!")
            return redirect("dashboard")

    context = {'add_client_form': form}

    return render(request, 'webapp/create-record.html', context=context)


# Update client record
@login_required(login_url='mylogin')
def update_client(request, pk):
    client = Client.objects.get(id=pk)

    form = UpdateClientForm(instance=client)

    if request.method == "POST":
        form = UpdateClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            messages.success(request, "Client Updated!")

            return redirect("dashboard")

    context = {'update_client_form': form}

    return render(request, 'webapp/update-record.html', context=context)


# Read Single Client Record
@login_required(login_url='mylogin')
def view_single_client(request, pk):
    all_clients = Client.objects.get(id=pk)


    context = {'client': all_clients}

    return render(request, 'webapp/view-record.html', context=context)

# Delete a client record
def delete_client(request, pk):
    client = Client.objects.get(id=pk)

    client.delete()
    messages.success(request, "Client Deleted!")

    return redirect('dashboard')



# Logout a user
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out!")

    return redirect("mylogin")