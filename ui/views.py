from django.shortcuts import render
from pymodbus.client.sync import ModbusTcpClient
from .models import Plc

def index(request):
	plc_db_list = Plc.objects.order_by('name')
	plc_list = []
	for plc in plc_db_list:
		client = ModbusTcpClient(plc.ip)
		if plc.number_of_coils:
			response = client.read_coils(plc.first_coil - 1, plc.number_of_coils)
			coils_list = response.bits[:plc.number_of_coils]
			first_coil = plc.first_coil
		else:
			first_coil = None
			coils_list = None
		if plc.number_of_discrete_inputs:
			response = client.read_discrete_inputs(plc.first_discrete_input - 1, plc.number_of_discrete_inputs)
			discrete_inputs_list = response.bits[:plc.number_of_discrete_inputs]
			first_discrete_input = plc.first_discrete_input
		else:
			first_discrete_input = None
			discrete_inputs_list = None
		if plc.number_of_discrete_inputs:
			response = client.read_holding_registers(plc.first_holding_register - 1, plc.number_of_holding_registers)
			holding_registers_list = response.registers[:plc.number_of_holding_registers]
			first_holding_register = plc.first_holding_register
		else:
			first_holding_register = None
			holding_registers_list = None
		if plc.number_of_input_registers:
			response = client.read_input_registers(plc.first_input_register - 1, plc.number_of_input_registers)
			input_registers_list = response.registers[:plc.number_of_input_registers]
			first_input_register = plc.first_input_register
		else:
			first_input_register = None
			input_registers_list = None
		client.close()
		plc_list.append({
			'name': plc.name,
			'ip': plc.ip,
			'first_coil': first_coil,
			'coils_list': coils_list,
			'first_discrete_input': first_discrete_input,
			'discrete_inputs_list': discrete_inputs_list,
			'first_holding_register': first_holding_register,
			'holding_registers_list': holding_registers_list,
			'first_input_register': first_input_register,
			'input_registers_list': input_registers_list
		})
	context = {
		'plc_list': plc_list
	}
	return render(request, 'ui/index.html', context)
def coils(request, first_coil, last_coil):
	number_of_coils = last_coil - first_coil
	client = ModbusTcpClient('127.0.0.1')
	result = client.read_coils(first_coil - 1, number_of_coils)
	client.close()
	context = {
		'coils': result.bits[:number_of_coils]
	}
	return render(request, 'ui/coils.html', context)