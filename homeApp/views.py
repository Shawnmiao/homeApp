
from django.shortcuts import render, redirect
from .forms import StaffHireForm
from django.http import HttpResponse
from .models import Staff

def index(request):
    return render(request, 'homeApp/index.html', {})


def hire_staff(request):
    if request.method == 'POST':
        form = StaffHireForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Staff hired successfully")
    else:
        form = StaffHireForm()

    return render(request, 'homeApp/staff_hiring.html', {'form': form})

# Create your views here.
def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'homeApp/staff_list.html', {'staff_list': staffs})


def update_staff(request, pk):
    staff = Staff.objects.get(staffno=pk)
    form = StaffHireForm(request.POST or None, instance=staff)

    if form.is_valid():
        form.save()
        return redirect('staff_list')

    return render(request, 'homeApp/staff_edit.html', {'form': form})