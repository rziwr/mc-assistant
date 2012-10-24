#-*- coding: utf-8 -*-
#from sensors_uni import *
import json

import usaio.io_wrapper as iow

# Читаем конфигурация сенсора
def get_sensors_cfg():
	sets = { 'name': 'sensors_cfg_names.json', 'howOpen': 'r', 'coding': 'cp1251'}
	readedList = iow.file2list( sets )
	sensor_sets = json.loads( ' '.join(readedList))
	print json.dumps(sensor_sets, sort_keys=True, indent=2)
	return sensor_sets
	
class SensorChannal():
	def __init__(self, sets, addacName, hxName):
		# Параметры делителя напряжения
		splitter_params = sensor_sets['splitter_params']
		R1 = splitter_params['R1']
		R2 = splitter_params['R2']
		splitter = R2/(R1+R2)

		# Параметры ADDAC
		addac = sensor_sets['addac']
		dVmax = addac[ 'dVmax' ]	# mV сдвиг ЦАП
		VmaxIdeal = addac[ 'VmaxIdeal' ]

		capacity = addac[ 'capacity' ]
		Vmax = VmaxIdeal-dVmax 	# mV - это максимальное значение ЦАП - площадка при выс. сигн.
		resolution = math.pow(2, capacity)

		toDigital = resolution/Vmax
		toAnalog = 1/toDigital
		
		
# Параметры входной кривой
# Датчик Холла
def value2voltageHall(value, sensor_sets):
	curve_params = sensor_sets['curve_params']
	Kiu = curve_params[ 'Kiu' ]		# mV/A
	dU = curve_params[ 'dU' ]		# mV
	U = I * Kiu + dU
	return U
	
value2voltage = value2voltageHall
	