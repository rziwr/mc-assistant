#-*- coding: utf-8 -*-
#from sensors_uni import *
import json
import math

import usaio.io_wrapper as iow
import simpleDataTypesConvertors.IntTypeConvertors as tc

# Читаем конфигурация сенсора
def get_sensors_cfg():
	sets = { 'name': 'sensors_cfg_names.json', 'howOpen': 'r', 'coding': 'cp1251'}
	readedList = iow.file2list( sets )
	sensor_sets = json.loads( ' '.join(readedList))
	print json.dumps(sensor_sets, sort_keys=True, indent=2)
	return sensor_sets
	
def get_sensor_cfg( name ):
	# читае общую конфигурацию
	uni_sensor_sets = get_sensors_cfg()
	sets = { 'name': 'sensors_cfg_names.json', 'howOpen': 'r', 'coding': 'cp1251'}
	# читаем конфигурацию для тока
	sets[ 'name' ] = uni_sensor_sets[name]
	sensorSettings = iow.file2list( sets )

	# here we are converting python object to json string
	sensor_sets = json.loads( ' '.join(sensorSettings))
	print json.dumps(sensor_sets, sort_keys=True, indent=2)
	return sensor_sets
	
class SensorChannalHall():
	_addac = None
	_splitter_params = None
	_sensor_curve_cb = None
	_sensor_curve_sets = None
	def __init__(self, sensor_sets, addacName, hxName, curve_cb ):
		# Параметры делителя напряжения
		self._splitter_params = sensor_sets[hxName]

		# Параметры ADDAC
		self._addac = sensor_sets[ addacName ]
		
		# кривая сенсора
		self._sensor_curve_cb = curve_cb
		self._sensor_curve_sets = sensor_sets['sensor_curve_params']

	def getSplitter( self ):
		R1 = self._splitter_params['R1']
		R2 = self._splitter_params['R2']
		splitter = R2/(R1+R2)
		return splitter
		
	def toBitCoeff( self ):
		dVmax = self._addac[ 'dVmax' ]	# mV сдвиг ЦАП
		VmaxIdeal = self._addac[ 'VmaxIdeal' ]

		capacity = self._addac[ 'capacity' ]
		Vmax = VmaxIdeal-dVmax 	# mV - это максимальное значение ЦАП - площадка при выс. сигн.
		resolution = math.pow(2, capacity)

		toDigital = resolution/Vmax
		return toDigital
	
	def getCapacity(self):
		return self._addac[ 'capacity' ]
		
	def toWaveCoeff( self ):
		return 1/self.toBitCoeff( )
		
	def sensor_curve(self, value):
		return self._sensor_curve_cb(value, self._sensor_curve_sets)
		
# Параметры входной кривой
# Датчик Холла
def value2voltageHall(value, curve_params):
	Kiu = curve_params[ 'Kiu' ]		# mV/A
	dU = curve_params[ 'dU' ]		# mV
	U = value * Kiu + dU
	return U
	
'''
	Ток в код и обратно I, A 
	код не переведен в цифру - предст. с плав. точкой 
'''
# Example:
# Uo = R16*Uerr/(R16+R10) = 10*500/(10+5.11) = 330.907 mV
# 2^10 - 5000 mV
# x - Uo ; x = 67.76 ue = 68 ue = 0x44 ue
def calcCoeffTransf( value, channal ):
	# Получаем описание канала и кривой сенсора
	multer = channal.getSplitter()
	toDigital = channal.toBitCoeff()
	
	# Обработка
	U = channal.sensor_curve( value )
	
	# Умножаем на коэфф. перед. аналоговой цепи и "оцифровываем"
	Uadc = U * multer * toDigital
	Udig = int( Uadc )
	return tc.byte4strhex( Udig ), str( channal.getCapacity() )	