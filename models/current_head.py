#-*- coding: utf-8 -*-
# from current_head import *
import math
import json

import usaio.io_wrapper as iow

# Читаем конфигурация сенсора
sets = { 'name': 'sensors_cfg_names.json', 'howOpen': 'r', 'coding': 'cp1251'}
uni_sensor_settings = iow.file2list( sets )
uni_sensor_sets = json.loads( ' '.join(uni_sensor_settings))
print json.dumps(uni_sensor_sets, sort_keys=True, indent=2)

sets[ 'name' ] = uni_sensor_sets['I']
sensorSettings = iow.file2list( sets )

# here we are converting python object to json string
sensor_sets = json.loads( ' '.join(sensorSettings))
print json.dumps(sensor_sets, sort_keys=True, indent=2)

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

# Параметры входной кривой
curve_params = sensor_sets['curve_params']
Kiu = curve_params[ 'Kiu' ]		# mV/A
dU = curve_params[ 'dU' ]		# mV

# Coeffs
resolution = math.pow(2, capacity)
toDigital = resolution/Vmax
toAnalog = 1/toDigital