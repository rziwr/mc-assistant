#-*- coding: utf-8 -*-
# core
# utils
from pyDbg.doColoredConsole import co
nprint = co.printN
wprint = co.printW
eprint = co.printE
	
import simpleDataTypesConvertors.Float32Convertors as f32cnv
import simpleDataTypesConvertors.IntTypeConvertors as tc

# Читаем конфигурация сенсора
from current_head import *

''' 
	Ток в код и обратно I, A 
	код не переведен в цифру - предст. с плав. точкой 
'''
def toDigitalFull( U, mult, toDigital ):
	Uadc = U * mult	# На плече делителя нужный нам потенц
	# ADC
	Udig = toDigital * Uadc
	return Udig
	
	
def wprintValue( name, value ):
	wprint( name+' : '+str(value)+'\n')
def calcCoeffTransf(I):
	# Исходная зашумленная зависимость
	multer = splitter	# если напрямую с датчик Холла
	U = I * Kiu + dU
	wprint( 'Udac : ' + str( U )+'\n')
	Udig_f = toDigitalFull( U, multer, toDigital )
	wprint( 'Udig_f, mC : '+str(Udig_f)+'\n')
	Udig = int( Udig_f )
	wprintValue( 'Udig, ue', Udig )
	
	# Рассчитываем шум - смещение по Y
	Udig_noise_f = toDigitalFull( dU, multer, toDigital )
	
	# Очищенное значение - без шума
	Udig_corr = int(Udig_f - Udig_noise_f)	# суммируются перед оцифровкой
	
	# переводим в плавающую точку
	print 'capacity : ' + str( capacity )
	nprint( 'Udig_src, ue : ' )
	eprint( tc.byte4strhex( Udig )+'\n')
	return Udig

# Run 
if __name__ == '__main__':
	# расчет коэффициентов трансформации
	listOfCurrents = [0]
	for current in listOfCurrents :
		msg = '\nI,A : ' + str( current ) + '\n'
		wprint( msg )
		print calcCoeffTransf( current ) 
