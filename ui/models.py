from django.db import models

class Plc(models.Model):
	name = models.CharField(max_length=64)
	ip = models.CharField(max_length=15, default='127.0.0.1')
	first_coil = models.IntegerField(default=1)
	number_of_coils = models.IntegerField(default=1)
	first_discrete_input = models.IntegerField(default=1)
	number_of_discrete_inputs = models.IntegerField(default=1)
	first_holding_register = models.IntegerField(default=1)
	number_of_holding_registers = models.IntegerField(default=1)
	first_input_register = models.IntegerField(default=1)
	number_of_input_registers = models.IntegerField(default=1)
	def __str__(self):
		return self.name