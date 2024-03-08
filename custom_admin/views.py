from django.shortcuts import render
from meatapp.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from meatapp.forms import CustomAdminRegistrationForm


def register_custom_admin(request):
    if request.method == 'POST':
        form = CustomAdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login') 
    else:
        form = CustomAdminRegistrationForm()
    return render(request, 'register_admin.html', {'form': form})


def custom_admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('order_list')  
        else:
            # Authentication failed
            return render(request, 'admin_login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'admin_login.html')


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('order_list')  

    return render(request, 'order_list.html', {'order': order})


def admin_logout_request(request):
    logout(request)
    return redirect('admin_login')