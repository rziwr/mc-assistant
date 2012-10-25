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

# читае конфигурация сенсора
sensor_sets = get_sensor_cfg('U')

# Настройки прочитаны, можно разбирать их
value2voltage = value2voltageHall
SensorChannal = SensorChannalHall

metroChannal = SensorChannal( sensor_sets,'adc_metro','splitter_metro_parems', value2voltage )
thresholdChannal_max = SensorChannal( sensor_sets,'dac_threshes','splitter_threshold_parems', value2voltage )
thresholdChannal_min = SensorChannal( sensor_sets,'dac_threshes','splitter_threshold_parems', value2voltage )

# Run 
if __name__ == '__main__':
	pass
'''
	# смещение нуля при обратоной обработке
	I = 0
	Udig_zero, capacity = calcCoeffTransf( I, metroChannal ) 
	# Записать в файл шаблон
	sets = { 'name': 'threshes.h', 'howOpen': 'w', 'coding': 'cp1251'}
	lstForWrite = list('')
	lstForWrite.append('#ifdef HALL_SENSORS')
	lstForWrite.append('\t#define ZERO_HALL_CORRECT '+Udig_zero+"\t;"+
		str(I)+" A; bits - "+capacity+'\n' )
	iow.list2file( sets=sets, lst=lstForWrite )
	
	# Пороги
	listOfCurrents = [16]
	lstForWrite = list('')
	# Записать в файл шаблон
	sets = { 'name': 'threshes.h', 'howOpen': 'a', 'coding': 'cp1251'}
	for I in listOfCurrents :
		wprintValue('\nI,A : ', I)
		Udig, capacity = calcCoeffTransf( I, thresholdChannal ) 
		eprintValue('U_code', Udig)
		lstForWrite.append('\t#define CURRENT_THR '+Udig+"\t;"+
			str(I)+" A  bits - "+capacity)
			
	# Находим коэффициент пересчета
	I = 10
	Udig_value, capacity = calcCoeffTransf( I, metroChannal ) 
	realCodeCurrent = tc.hex_word_to_uint(Udig_value)-tc.hex_word_to_uint(Udig_zero)
	k = I/realCodeCurrent
	wprintValue('K code to A :', k)
	
	lstForWrite.append(';const double TA_CURRENT_MUL = '+str(k)+';')

	# Закрываем запись
	lstForWrite.append('#endif ;HALL_SENSOR\n')
	iow.list2file( sets=sets, lst=lstForWrite )'''

