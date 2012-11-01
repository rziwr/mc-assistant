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
sensor_sets = get_sensor_cfg('I')

# Настройки прочитаны, можно разбирать их
value2voltage = value2voltageHall
SensorChannal = SensorChannalHall

metroChannal = SensorChannal( sensor_sets,'adc_metro','splitter_metro_parems', value2voltage )
thresholdChannal = SensorChannal( sensor_sets,'dac_threshes','splitter_threshold_parems', value2voltage )

# Run 
if __name__ == '__main__':

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
	listOfCurrents = [20, 22]
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
	print Udig_value
	realCodeCurrent = tc.hex_word_to_uint(Udig_value)-tc.hex_word_to_uint(Udig_zero)
	k = I/realCodeCurrent
	wprintValue('K code to A :', k)
	
	lstForWrite.append(';const double TA_CURRENT_MUL = '+str(k)+';')

	# Закрываем запись
	lstForWrite.append('#endif ;HALL_SENSOR\n')
	iow.list2file( sets=sets, lst=lstForWrite )
	

''' 
# коэффициент перевода. Это чистое значение тока - для рассчетов и отображения
# Warning : немного расходится с прошитым, но прошитый откалиброван, поэтому 
#   наверное пусть как есть
Ktrans = I/Udig_corr  # A/ue

# переводим в плавающую точку
print 'capacity : ' + str( capacity )
co.printN( 'Udig_src, ue : ' )
co.printE( tc.byte4strhex( Udig )+'\n')

msg = "Tr. I,A="
msg = msgSplit(msg)
f = open('treshes.log', 'at');
ILow = I%10
IHigh = (I-ILow)/10
f.write("\t#define I_MSG_HIGH '"+str(IHigh)+"'\n")
f.write("\t#define I_MSG_LOW '"+str(ILow)+"'\n")
#f.write("; "+msg+"I_MSG_HIGH,I_MSG_LOW"+",'/'\n")
f.write( '\t#define CURRENT_THRESHOLD '+tc.byte4strhex( Udig )+"\t;"+str(I)+" A"+"\n\n")
f.close()
#print 'Udig_cor, ue :  ' + tc.byte4strhex( Udig_corr )
return Udig

'' ' Просто заглушка '' '
def printRpt( value, valueDisplacemented, valueScaled, valueCode, Kda ):
	print '\n<< Output values:'
	print 'Code : '+str(valueCode)
	print 'Kda : '+str(Kda)
'''
#import ModelADDAC as adda
# проверяем
'''valueDict = {}
valueDict[ 'value' ] = I
valueDict['displacement'] = dU
valueDict['converter' ] = Kiu
valueDict['scale'] = Splitter
valueDict['capacity'] = capacity
valueDict['Vmax'] = Vmax 
code, Kda = adda.modelADC( valueDict, printRpt, adda.calcZeroDisplacmentY )'''
