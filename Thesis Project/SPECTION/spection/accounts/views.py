

import datetime
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import *

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
)

from django.conf import settings

from .filters import Orderfilter
import json
import sys
import re
# Create your views here.


def home(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment is successfully send!')
            return redirect('home')
        else:
            messages.error(request, 'Appointment is invalid!')
    return render(request, 'accounts/pages/home.html')


def post(request):
    news = News.objects.all()
    news = news.filter(headline=True)
    total_news = news.count() + 1
    total = []
    for num in range(1, total_news):
        total.append(num)
    print(total)
    context = {
        'news': news,
        'total_news': total,
    }
    return render(request, 'accounts/pages/post.html', context)


def calendar(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment is successfully send!')
            return redirect('calendar')
        else:
            messages.error(request, 'Appointment is invalid!')
    return render(request, 'accounts/pages/calendar.html')


def contact(request):
    return render(request, 'accounts/pages/contacts.html')


def about(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment is successfully send!')
            return redirect('about')
        else:
            messages.error(request, 'Appointment is invalid!')
    return render(request, 'accounts/pages/about.html')


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            fname = request.user.first_name
            lname = request.user.last_name
            messages.success(request, fname + ' ' +
                             lname + ' has been logged in!')
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == "patient":
                    return redirect('patient')
                if group == "admin":
                    return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'accounts/pages/login.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patient(request):
    patient = request.user.patient
    form = PatientForm(instance=patient)
    orders = request.user.patient.order_set.all()

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            messages.success(request, ' has logged out!')
            form.save()

    context = {

        'orders': orders,
        'form': form,
    }
    return render(request, 'accounts/pages/patient_panel.html', context)


def logoutUser(request):
    group = None
    # if request.user.groups.exists():
    #     group = request.user.groups.all()[0].name
    #     if group == "patient":
    #         name = request.user.patient.name
    #     if group == "admin":
    #         name = 'Admin'

    messages.success(request,  ' User has logged out!')
    logout(request)
    return redirect('login')

# Admin Panel


def appointment(request):
    order_by_list = ['-date', '-time']
    appoint = Appointment.objects.all()
    appointments = appoint.order_by(*order_by_list)

    context = {
        'appointments': appointments,
    }
    return render(request, 'admin/pages/appointment.html', context)


def create_billing(request):
    return render(request, 'admin/forms/create_billing.html')


def billing(request):
    return render(request, 'admin/pages/billing.html')


def dues(request):
    return render(request, 'admin/pages/dues.html')


def schedule(request):
    schedule = Schedule.objects.all()
    dictionary = list(schedule.values_list())
    list_result = [list(entry) for entry in dictionary]
    list_result = [{'id': entry[0], 'name':entry[1], 'badge':entry[2], 'date':entry[3], 'type':entry[4], 'everyYear':entry[5], 'description':entry[6], 'color':entry[7]}
                   for entry in list_result]
    sys.stdout = open(settings.STATICFILES_DIRS[0] + '/js/admin.js', 'w')
    jsonobj = json.dumps(list_result)
    print("var jsonstr = '{0}'".format(jsonobj))

    context = {'schedule': schedule}
    return render(request, 'admin/pages/schedule.html', context)


def create_schedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        type = request.POST['type']
        from_date = request.POST['date']
        to_date = request.POST['to_date']
        if to_date != '':
            date = from_date + ':' + to_date
        else:
            date = from_date
        if type == 'Event':
            color = '#dc0000'
        elif type == 'Holiday':
            color = '#ffa808'
        else:
            color = '#40a900'
        print(to_date)
        if form.is_valid():
            sched = form.save(commit=False)
            sched.color = color
            sched.date = date
            sched.save()
            messages.success(request, 'Post is successfully send!')
            return redirect('schedule')
        else:
            error = " & ".join(form.errors)

            messages.error(
                request, error + ' is Invalid.')
    context = {
        'form': form,
    }
    return render(request, 'admin/forms/create_schedule.html', context)


def update_schedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    form = ScheduleForm(instance=schedule)
    schedule_date = schedule.date.split(':')
    to_date = ''
    date_count = len(schedule_date)
    if len(schedule_date) == 1:
        from_date = schedule_date[0]
    else:
        from_date = schedule_date[date_count-2]
        to_date = schedule_date[date_count-1]
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=schedule)
        type = request.POST['type']
        from_date = request.POST['date']
        to_date = request.POST['to_date']
        if to_date != '':
            date = from_date + ':' + to_date
        else:
            date = from_date
        if to_date != '':
            date = from_date + ':' + to_date
        else:
            date = from_date
        if type == 'Event':
            color = '#dc0000'
        elif type == 'Holiday':
            color = '#ffa808'
        else:
            color = '#40a900'
        if form.is_valid():
            sched = form.save(commit=False)
            sched.color = color
            sched.date = date
            sched.save()
            messages.success(
                request, 'Schedule Event has been successfully Updated!')
            return redirect('schedule')
        else:
            error = " & ".join(form.errors)

            messages.error(
                request, error + ' is Invalid.')
    context = {
        'schedule': schedule, 'form': form, 'from_date': from_date, 'to_date': to_date,

    }
    return render(request, 'admin/forms/update_schedule.html', context)


def delete_schedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    if request.method == "POST":
        schedule.delete()
        messages.success(request, 'Schedule Event has been Deleted!')
        return redirect('schedule')

    context = {'item': schedule}
    return render(request, 'admin/forms/delete_schedule.html', context)


def news(request):
    order_by_list = ['-date_created']
    new = News.objects.all()
    news = new.order_by('-date_created')
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'News is successfully created!')
            return redirect('news')
        else:
            messages.error(request, 'News not Created!')
    context = {
        'news': news,
        'form': form,
    }
    return render(request, 'admin/pages/announcement.html', context)


def create_news(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post is successfully send!')
            return redirect('news')
        else:
            messages.error(request, 'Fields are invalid!')
    context = {
        'form': form,
    }
    return render(request, 'admin/forms/create_news.html', context)


def delete_news(request, pk):
    news = News.objects.get(id=pk)
    if request.method == "POST":
        news.delete()
        messages.success(request, 'News has been Deleted!')
        return redirect('news')

    context = {'item': news}
    return render(request, 'admin/forms/delete_news.html', context)


def update_news(request, pk):
    news = News.objects.get(id=pk)
    form = NewsForm(instance=news)

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'News has been successfully Updated!')
            return redirect('news')
        else:
            error = " & ".join(form.errors)

            messages.error(
                request, error + ' is Invalid.')
    context = {
        'news': news,
        'form': form,
    }
    return render(request, 'admin/forms/update_news.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def register(request):
    form = CreateUserForm()
    form_2 = AccountForm()
    models = [Patient, History]
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        form_2 = AccountForm(request.POST)

        if form.is_valid() and form_2.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            account = form_2.save(commit=False)
            account.user = user
            account.save()

            for model in models:
                model.objects.create(user=user,)
            messages.success(request, 'Account was created for ' + username)
            return redirect('/patient_list/')
        else:
            error = " & ".join(form.errors)
            error2 = " & ".join(form_2.errors)

            messages.error(
                request, error + error2 + ' is Invalid.')

    context = {
        'form': form,
        'patient_form': form_2,
    }
    return render(request, 'admin/pages/registration.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    patients = Patient.objects.all()
    total_patient = patients.count()
    context = {'total_patient': total_patient}
    return render(request, 'admin/pages/dashboard.html', context)

# Patient


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def patient_list(request):
    patients = Account.objects.all()
    context = {'patients': patients}
    return render(request, 'admin/pages/patient_list.html', context)


def deletePatient(request, pk):
    patient = Account.objects.get(id=pk)
    user = User.objects.get(username=patient)

    if request.method == "POST":
        user.delete()
        messages.success(request, 'Patient has been Deleted!')
        return redirect('patient list')

    context = {'patient': patient}
    return render(request, 'admin/forms/delete_patient.html', context)


def person_info(request, pk):
    patient = Account.objects.get(id=pk)
    context = {'patient': patient}
    return render(request, 'admin/components/person_info.html', context)


def update_info(request, pk):
    patient = Account.objects.get(id=pk)
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Case History has been successfully Updated!')
            return redirect('/patient_list/patient/' + pk + '/Information/')
        else:
            error = " & ".join(form.errors)

            messages.error(
                request, error + ' is Invalid.')
    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'admin/forms/update_info.html', context)


def person_list_case(request, pk):
    patient = Account.objects.get(id=pk)
    user = User.objects.get(username=patient)
    cases = Case.objects.all().filter(user=user)
    context = {
        'patient': patient,
        'cases': cases,
    }
    return render(request, 'admin/components/person_list_case.html', context)


def person_list_rx(request, pk):
    patient = Account.objects.get(id=pk)
    user = User.objects.get(username=patient)
    prescriptions = Rx.objects.all().filter(user=user).order_by('-date_created')
    total_prescriptions = prescriptions.count()
    context = {
        'patient': patient,
        'prescriptions': prescriptions,
        'total_prescriptions': total_prescriptions
    }
    return render(request, 'admin/components/person_list_rx.html', context)


def create_rx(request, pk):
    patient = Account.objects.get(id=pk)
    user = User.objects.get(username=patient)
    form = RxForm()
    if request.method == "POST":

        form = RxForm(request.POST,)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = user
            candidate.save()
            messages.success(request, 'New case has been created!')

            return redirect('/patient_list/patient/' + pk + '/RX/')

    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'admin/forms/create_rx_form.html', context)


def update_rx(request, pk, rx_id):
    patient = Account.objects.get(id=pk)
    user = User.objects.get(username=patient)
    rx = Rx.objects.get(id=rx_id)
    form = RxForm()
    if request.method == "POST":
        form = RxForm(request.POST, instance=rx)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = user
            candidate.save()
            messages.success(
                request, 'Prescription has been successfully Updated!')
            return redirect('/patient_list/patient/' + pk + '/RX/')
        else:
            messages.error(request, 'Input Fields Error!')
    context = {
        'patient': patient,
        'rx': rx,
        'form': form,
    }
    return render(request, 'admin/forms/update_rx_form.html', context)


def delete_rx(request, pk, rx_id):
    patient = Account.objects.get(id=pk)
    rx = Rx.objects.get(id=rx_id)
    if request.method == "POST":
        rx.delete()
        messages.success(request, 'Prescription has been Deleted!')
        return redirect('/patient_list/patient/' + pk + '/RX/')
    context = {
        'patient': patient,
        'rx': rx,
    }
    return render(request, 'admin/forms/delete_rx.html', context)


def person_case(request, pk, case_id):
    patient = Account.objects.get(id=pk)

    case = Case.objects.get(id=case_id)
    signs = Signs.objects.get(user=case)
    refract = Refraction.objects.get(user=case)
    cover_test = CoverTest.objects.get(user=case)
    pupil_reflex = PupilReflex.objects.get(user=case)
    pupil_measure = PupilMeasurement.objects.get(user=case)
    history = History.objects.get(user=case)
    form = SignsForm()

    signs_list = signs.signs_details.split(":")
    visual_task_list = signs.activity_details.split(":")

    context = {
        'patient': patient,
        'case': case,
        'signs': signs, 'signs_list': signs_list, 'visual_task_list': visual_task_list,
        'refract': refract, 'cover_test': cover_test, 'pupil_reflex': pupil_reflex, 'pupil_measure': pupil_measure, 'history': history,
        'form': form,
    }
    return render(request, 'admin/components/person_case.html', context)


def create_case(request, pk):
    patient = Account.objects.get(id=pk)
    user = User.objects.get(username=patient)
    models = [Signs, Refraction, CoverTest,
              PupilReflex, PupilMeasurement, History]
    form = CaseForm()
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            messages.success(request, 'New case has been created!')
            case = Case.objects.create(user=user,)
            for model in models:
                model.objects.create(user=case,)

        return redirect('/patient_list/patient/' + pk + '/Case/')

    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'admin/forms/case_form.html', context)


def update_case(request, pk, case_id):
    patient = Account.objects.get(id=pk)
    case = Case.objects.get(id=case_id)
    signs = Signs.objects.get(user=case)
    refract = Refraction.objects.get(user=case)
    cover_test = CoverTest.objects.get(user=case)
    pupil_reflex = PupilReflex.objects.get(user=case)
    pupil_measure = PupilMeasurement.objects.get(user=case)
    history = History.objects.get(user=case)

    history_form = HistoryForm()
    refract_form = RefractionForm()
    cover_test_form = CoverTestForm()
    pupil_reflex_form = PupilReflexForm()
    pupil_measure_form = PupilMeasurementForm()
    signs_form = SignsForm()

    signs_list = signs.signs_details.split(":")
    visual_task = signs.activity_details.split(":")

    symptoms_list = ['Headache Frontal', 'Headache Temporal', 'Headache Occipital', 'Headache Intraocular',
                     'Headache Parietal', 'Headache Intermittent', 'Headache Recurrent', 'Headache Constant', 'After Reading', 'Granulation', 'Eye Strain', 'Ptosis']

    visual_task_list = ['Reading', 'Computing', 'Writing', 'Others']

    if request.method == 'POST':
        signs_form = SignsForm(request.POST, instance=signs)
        history_form = HistoryForm(request.POST, instance=history)
        refract_form = RefractionForm(request.POST, instance=refract)
        cover_test_form = CoverTestForm(request.POST, instance=cover_test)
        pupil_reflex_form = PupilReflexForm(
            request.POST, instance=pupil_reflex)
        pupil_measure_form = PupilMeasurementForm(
            request.POST, instance=pupil_measure)

        symptoms = request.POST.getlist('symptoms')
        visual_task = request.POST.getlist('visual_task')
        signs_string = ":".join(symptoms)
        visual_task_string = ":".join(visual_task)

        forms = [refract_form, cover_test_form,
                 pupil_reflex_form, pupil_measure_form, history_form]
        if refract_form.is_valid() and cover_test_form.is_valid():
            for form in forms:
                form.save()
            signs_d = signs_form.save(commit=False)
            signs_d.signs_details = signs_string
            signs_d.activity_details = visual_task_string
            signs_d.save()
            messages.success(
                request, 'Case History has been successfully Updated!')
            return redirect('/patient_list/patient/' + pk + '/Case/' + case_id + '/')
        else:
            errors = []
            for form in forms:
                error = " & ".join(form.errors)
                errors += error
            errors = " & ".join(errors.errors)
            messages.error(
                request, errors + ' is Invalid.')

    context = {
        'patient': patient, 'others': visual_task[-1],
        'case': case, 'signs_form': signs_form, 'signs_list': signs_list, 'symptoms_list': symptoms_list, 'visual_task_list': visual_task_list, 'visual_task': visual_task,
        'refract': refract, 'cover_test': cover_test, 'pupil_reflex': pupil_reflex, 'history': history, 'history_form': history_form,
        'refract_form': refract_form, 'cover_test_form': cover_test_form, 'pupil_reflex_form': pupil_reflex_form, 'pupil_measure': pupil_measure,
    }

    return render(request, 'admin/forms/update_case.html', context)


def delete_case(request, pk, case_id):
    patient = Account.objects.get(id=pk)
    case = Case.objects.get(id=case_id)
    if request.method == "POST":
        case.delete()
        messages.success(request, 'Case has been Deleted!')
        return redirect('/patient_list/patient/' + pk + '/Case/')

    context = {
        'patient': patient,
        'case': case,
    }
    return render(request, 'admin/forms/case_delete_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'admin/pages/products.html', context)


class BookCreateView(BSModalCreateView):
    template_name = 'admin/components/create_order.html'
    form_class = CreateModalForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('orders')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def orders(request):
    orders = Order.objects.all()
    myFilter = Orderfilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'admin/pages/orders.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order has been successfully Updated!')
            return redirect('orders')
        else:
            messages.error(request, 'Input Fields Error!')

    context = {'form': form}

    return render(request, 'admin/forms/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        messages.success(request, 'Order has been Deleted!')
        return redirect('orders')

    context = {'item': order}
    return render(request, 'admin/forms/delete.html', context)
