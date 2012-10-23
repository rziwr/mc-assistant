#-*- coding: utf-8 -*-
import usaio.io_wrapper

# core
import math

# utils
from pyDbg.doColoredConsole import co
import simpleDataTypesConvertors.Float32Convertors as f32cnv
import simpleDataTypesConvertors.IntTypeConvertors as tc


# Mults
R1 = 5.11
R2 = 10.0
Splitter = R2/(R1+R2)

# Параметры ADDAC
dVmax = 430.0	# mV сдвиг ЦАП
VmaxIdeal = 5000.0
Vmax = VmaxIdeal-dVmax 	# mV - это максимальное значение ЦАП - площадка при выс. сигн.
Vmax = VmaxIdeal 
capacity = 12

# Параметры входной кривой
Kiu = 188.0		# mV/A
dU = 500.0		# mV

# Deprecated
Resol = math.pow(2, capacity)
toDigital = Resol/Vmax#/VmaxIdeal
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
