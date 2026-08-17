from django.urls import path
from . import views


urlpatterns = [

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # Employees

    path(
        'employees/',
        views.employee_list,
        name='employee_list'
    ),

    path(
        'employees/add/',
        views.employee_create,
        name='employee_create'
    ),

    path(
        'employees/<int:id>/',
        views.employee_detail,
        name='employee_detail'
    ),

    path(
        'employees/edit/<int:id>/',
        views.employee_update,
        name='employee_update'
    ),

    path(
        'employees/delete/<int:id>/',
        views.employee_delete,
        name='employee_delete'
    ),

    # Departments

    path(
        'departments/',
        views.department_list,
        name='department_list'
    ),

    path(
        'departments/add/',
        views.department_create,
        name='department_create'
    ),

    path(
        'departments/<int:id>/',
        views.department_detail,
        name='department_detail'
    ),

    path(
        'departments/edit/<int:id>/',
        views.department_update,
        name='department_update'
    ),

    path(
        'departments/delete/<int:id>/',
        views.department_delete,
        name='department_delete'
    ),

     path('logout/', 
     views.logout_view, 
     name='logout'),
]