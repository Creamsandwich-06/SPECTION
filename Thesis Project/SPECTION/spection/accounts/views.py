
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

from .models import *

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView

from .filters import Orderfilter

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'accounts/pages/home.html')


def calendar(request):
    return render(request, 'accounts/pages/calendar.html')


def contact(request):
    return render(request, 'accounts/pages/contacts.html')


def about(request):
    return render(request, 'accounts/pages/about.html')


def login(request):
    return render(request, 'accounts/pages/login.html')


def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    orders = patient.order_set.all()

    context = {
        'patient': patient,
        'orders': orders,
    }
    return render(request, 'accounts/pages/patient_panel.html', context)


# Admin Panel
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('register')

    context = {'forms': form}
    return render(request, 'admin/pages/registration.html', context)


def dashboard(request):
    patients = Patient.objects.all()
    total_patient = patients.count()
    context = {'total_patient': total_patient}
    return render(request, 'admin/pages/dashboard.html', context)


def patient_list(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'admin/pages/patient_list.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'admin/pages/products.html', context)


class BookCreateView(BSModalCreateView):
    template_name = 'admin/components/create_order.html'
    form_class = OrderForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('orders')


def orders(request):
    orders = Order.objects.all()

    myFilter = Orderfilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'admin/pages/orders.html', context)
