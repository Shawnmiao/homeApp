
from django.shortcuts import render, redirect
from .forms import StaffHireForm,BranchForm
from django.http import HttpResponse
from .models import Staff,Branch
from django.shortcuts import render, get_object_or_404, redirect
from .models import Branch
from django.urls import reverse
from django.http import HttpResponseRedirect

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
def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'homeApp/branch_list.html', {'branches': branches})

# def branch_edit(request, branchno):
#     branch = get_object_or_404(Branch, pk=branchno)
#     if request.method == 'POST':
#         branch.street = request.POST.get('street')
#         branch.city = request.POST.get('city')
#         branch.postcode = request.POST.get('postcode')
#         branch.save()
#         return HttpResponseRedirect(reverse('branch_list'))
#     return render(request, 'branch_edit.html', {'branch': branch})
def branch_edit(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')  # Redirect to the list view after saving
    else:
        form = BranchForm(instance=branch)

    return render(request, 'homeApp/branch_edit.html', {'form': form})
def branch_new(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')  # Redirect to the newly created branch's detail view
    else:
        form = BranchForm()  # An empty form for a new branch

    return render(request, 'homeApp/branch_new.html', {'form': form})

