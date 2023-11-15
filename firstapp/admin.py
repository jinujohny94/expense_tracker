from django.contrib import admin

# Register your models here.
from firstapp.models import Employer, Employee
admin.site.register(Employer)
admin.site.register(Employee)
