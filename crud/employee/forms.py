from django import forms
from employee.models import Employee, Vacation
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =  '__all__'


class VacationForm(forms.ModelForm):
     class Meta:
        model = Vacation
        fields = ['employee_id', 'from_date', 'to_date', 'reason']
