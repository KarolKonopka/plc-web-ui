from django.contrib import admin
from .models import Plc

class PlcAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip', 'first_coil', 'number_of_coils', 'first_discrete_input', 'number_of_discrete_inputs', 'first_holding_register', 'number_of_holding_registers', 'first_input_register', 'number_of_input_registers')
admin.site.register(Plc, PlcAdmin)