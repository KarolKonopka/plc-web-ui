from django.shortcuts import get_object_or_404, render
from pymodbus.client.sync import ModbusTcpClient
from .models import Plc

def index(request):
	plc_db_list = Plc.objects.order_by('name')
	plc_list = []
	for plc in plc_db_list:
		try:
			client = ModbusTcpClient(plc.ip)
			response = client.read_coils(0, 1)
			response.bits[0]
		except:
			plc_list.append({
				'id': plc.id,
				'name': plc.name,
				'ip': plc.ip,
				'connected': False,
			})
		else:
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
			plc_list.append({
				'id': plc.id,
				'name': plc.name,
				'ip': plc.ip,
				'connected': True,
				'first_coil': first_coil,
				'coils_list': coils_list,
				'first_discrete_input': first_discrete_input,
				'discrete_inputs_list': discrete_inputs_list,
				'first_holding_register': first_holding_register,
				'holding_registers_list': holding_registers_list,
				'first_input_register': first_input_register,
				'input_registers_list': input_registers_list
			})
			client.close()
	context = {
		'plc_list': plc_list
	}
	return render(request, 'ui/index.html', context)

def edit(request, plc_id):
	plc = get_object_or_404(Plc, pk=plc_id)
	try:
		client = ModbusTcpClient(plc.ip)
		response = client.read_coils(0, 1)
		response.bits[0]
	except:
		context = {
			'id': plc.id,
			'name': plc.name,
			'ip': plc.ip,
			'connected': False,
		}
	else:
		try: 
			edit_coil = int(request.POST['coil'])
		except KeyError:
			pass
		else:
			response = client.read_coils(edit_coil - 1, 1)
			edit_coil_value = response.bits[0]
			client.write_coil(edit_coil - 1, not edit_coil_value)
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
		context = {
			'id': plc.id,
			'name': plc.name,
			'ip': plc.ip,
			'connected': True,
			'first_coil': first_coil,
			'coils_list': coils_list,
			'first_discrete_input': first_discrete_input,
			'discrete_inputs_list': discrete_inputs_list,
			'first_holding_register': first_holding_register,
			'holding_registers_list': holding_registers_list,
			'first_input_register': first_input_register,
			'input_registers_list': input_registers_list
		}
		client.close()
	return render(request, 'ui/edit.html', context)