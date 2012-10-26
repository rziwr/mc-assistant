#-*- coding: utf-8 -*-
# core
# utils
from pyDbg.doColoredConsole import co
nprint = co.printN
wprint = co.printW
eprint = co.printE
def eprintValue( name, value ):
	eprint( name+' : '+str(value)+'\n')
def wprintValue( name, value ):
	wprint( name+' : '+str(value)+'\n')
def nprintValue( name, value ):
	nprint( name+' : '+str(value)+'\n')
	
import simpleDataTypesConvertors.Float32Convertors as f32cnv
import simpleDataTypesConvertors.IntTypeConvertors as tc

# Читаем конфигурация сенсора
import json

# Общая читалка
from sensors_uni import *

'''def value2voltageHall(value, curve_params):
	Kiu = curve_params[ 'Kiu' ]		# mV/A
	dU = curve_params[ 'dU' ]		# mV
	U = value * Kiu + dU
	return U'''

# читае конфигурация сенсора
sensor_sets = get_sensor_cfg('U')


# Настройки прочитаны, можно разбирать их
value2voltage = value2voltageHall
SensorChannal = SensorChannalHall

metroChannal = SensorChannal( sensor_sets,'adc_metro','splitter_metro_parems', value2voltage )
#thresholdChannal_max = SensorChannal( sensor_sets,'dac_threshes','splitter_threshold_parems', value2voltage )
#thresholdChannal_min = SensorChannal( sensor_sets,'dac_threshes','splitter_threshold_parems', value2voltage )

# Run 
if __name__ == '__main__':
	lstForWrite = list('')
	sets = { 'name': 'voltage_header.h', 'howOpen': 'w', 'coding': 'cp1251'}
	
	# смещение нуля при обратоной обработке
	U = 0
	Udig_zero, capacity = calcCoeffTransf( U, metroChannal ) 
	# Записать в файл шаблон
	lstForWrite = list('')
	lstForWrite.append('\t#define ZERO_VOLTAGE_CORRECT '+Udig_zero+"\t;"+str(U)+" V; bits - "+capacity+'\n' )
	
	'''# Пороги
	listOfCurrents = [16]
	
	# Записать в файл шаблон
	sets = { 'name': 'threshes.h', 'howOpen': 'a', 'coding': 'cp1251'}
	for I in listOfCurrents :
		wprintValue('\nI,A : ', I)
		Udig, capacity = calcCoeffTransf( I, thresholdChannal ) 
		eprintValue('U_code', Udig)
		lstForWrite.append('\t#define CURRENT_THR '+Udig+"\t;"+
			str(I)+" A  bits - "+capacity)'''
			
	# Находим коэффициент пересчета
	U = 48.0
	Udig_value, capacity = calcCoeffTransf( U, metroChannal ) 
	lstForWrite.append('\t#define TEST_MOCK_VOLTAGE '+Udig_value+"\t;"+str(U)+" V; bits - "+capacity+'\n' )
	
	realCodeVoltage = tc.hex_word_to_uint(Udig_value)-tc.hex_word_to_uint(Udig_zero)
	k = U/realCodeVoltage
	wprintValue('K code to V :', k)
	
	lstForWrite.append(';const double TA_VOLTAGE_MUL = '+str(k)+';')

	# Закрываем запись
	iow.list2file( sets=sets, lst=lstForWrite )

