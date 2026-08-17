from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Sum

from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm


# ==================================================
# DASHBOARD
# ==================================================

def dashboard(request):

    total_employees = Employee.objects.count()

    total_departments = Department.objects.count()

    total_salary = Employee.objects.aggregate(
        total=Sum('salary')
    )['total'] or 0

    context = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'total_salary': total_salary,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


# ==================================================
# EMPLOYEE LIST
# ==================================================

def employee_list(request):

    employees = Employee.objects.select_related(
        'department'
    ).order_by('name')

    search = request.GET.get('search', '')

    if search:
        employees = employees.filter(
            name__icontains=search
        )

    context = {
        'employees': employees,
        'search': search,
    }

    return render(
        request,
        'employee_list.html',
        context
    )


# ==================================================
# ADD EMPLOYEE
# ==================================================

def employee_create(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'employee_list'
            )

    else:

        form = EmployeeForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'employee_form.html',
        context
    )


# ==================================================
# EMPLOYEE DETAIL
# ==================================================

def employee_detail(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    context = {
        'employee': employee,
    }

    return render(
        request,
        'employee_detail.html',
        context
    )


# ==================================================
# EDIT EMPLOYEE
# ==================================================

def employee_update(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():

            form.save()

            return redirect(
                'employee_detail',
                id=employee.id
            )

    else:

        form = EmployeeForm(
            instance=employee
        )

    context = {
        'form': form,
        'employee': employee,
    }

    return render(
        request,
        'employee_form.html',
        context
    )


# ==================================================
# DELETE EMPLOYEE
# ==================================================

def employee_delete(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    if request.method == 'POST':

        employee.delete()

        return redirect(
            'employee_list'
        )

    context = {
        'employee': employee,
    }

    return render(
        request,
        'employee_delete.html',
        context
    )


# ==================================================
# DEPARTMENT LIST
# ==================================================

def department_list(request):

    departments = Department.objects.annotate(
        employee_count=Count('employees')
    ).order_by('name')

    search = request.GET.get('search', '')

    if search:

        departments = departments.filter(
            name__icontains=search
        )

    context = {
        'departments': departments,
        'search': search,
    }

    return render(
        request,
        'department_list.html',
        context
    )


# ==================================================
# ADD DEPARTMENT
# ==================================================

def department_create(request):

    if request.method == 'POST':

        form = DepartmentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'department_list'
            )

    else:

        form = DepartmentForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'department_form.html',
        context
    )


# ==================================================
# DEPARTMENT DETAIL
# ==================================================

def department_detail(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    employees = department.employees.all().order_by(
        'name'
    )

    context = {
        'department': department,
        'employees': employees,
    }

    return render(
        request,
        'department_detail.html',
        context
    )


# ==================================================
# EDIT DEPARTMENT
# ==================================================

def department_update(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    if request.method == 'POST':

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():

            form.save()

            return redirect(
                'department_detail',
                id=department.id
            )

    else:

        form = DepartmentForm(
            instance=department
        )

    context = {
        'form': form,
        'department': department,
    }

    return render(
        request,
        'department_form.html',
        context
    )


# ==================================================
# DELETE DEPARTMENT
# ==================================================

def department_delete(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    if request.method == 'POST':

        department.delete()

        return redirect(
            'department_list'
        )

    context = {
        'department': department,
        'employee_count': department.employees.count(),
    }

    return render(
        request,
        'department_delete.html',
        context
    )
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('login') 