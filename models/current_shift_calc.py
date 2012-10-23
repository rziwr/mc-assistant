#-*- coding: utf-8 -*-
# core
import math
import json

# utils
import usaio.io_wrapper as iow
from pyDbg.doColoredConsole import co
import simpleDataTypesConvertors.Float32Convertors as f32cnv
import simpleDataTypesConvertors.IntTypeConvertors as tc

# Читаем конфигурация сенсора
sets = { 'name': 'current_sensor.cfg', 'howOpen': 'r', 'coding': 'cp1251'}
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


''' Ток в код и обратно I, A '''
''' код не переведен в цифру - предст. с плав. точкой '''
def toDigitalFull( U, mult, toDigital ):
	Uadc = U * mult	# На плече делителя нужный нам потенц
	# ADC
	Udig = toDigital * Uadc
	return Udig
	
def calcCoeffTransf(I):
	# Исходная зашумленная зависимость
	multer = 1	# если напрямую с датчик Холла
	U = I * Kiu + dU
	co.printW( 'Udac : ' + str( U )+'\n')
	Udig_f = toDigitalFull( U, multer, toDigital )
	Udig = int( Udig_f )
	
	# Рассчитываем шум - смещение по Y
	Udig_noise_f = toDigitalFull( dU, multer, toDigital )
	
	# Очищенное значение - без шума
	Udig_corr = int(Udig_f - Udig_noise_f)	# суммируются перед оцифровкой

	# коэффициент перевода. Это чистое значение тока - для рассчетов и отображения
	# Warning : немного расходится с прошитым, но прошитый откалиброван, поэтому 
	#   наверное пусть как есть
	Ktrans = I/Udig_corr  # A/ue
	
	# переводим в плавающую точку
	print 'capacity : ' + str( capacity )
	co.printN( 'Udig_src, ue : ' )
	co.printE( tc.byte4strhex( Udig )+'\n')
	return Udig

''' Просто заглушка '''
def printRpt( value, valueDisplacemented, valueScaled, valueCode, Kda ):
	print '\n<< Output values:'
	print 'Code : '+str(valueCode)
	print 'Kda : '+str(Kda)

# Run 
if __name__ == '__main__':
	# расчет коэффициентов трансформации
	listOfCurrents = [15, 10, 5]
	for current in listOfCurrents :
		msg = '\nI,A : ' + str( current ) + '\n'
		co.printW( msg )
		print calcCoeffTransf( current ) 
