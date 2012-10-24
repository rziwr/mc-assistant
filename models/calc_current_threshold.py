#-*- coding: utf-8 -*-
# core
# utils
from pyDbg.doColoredConsole import co
nprint = co.printN
wprint = co.printW
eprint = co.printE
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
metroChannal = SensorChannal( sensor_sets,'adc_metro','splitter_metro_parems', value2voltage )

''' 
	Ток в код и обратно I, A 
	код не переведен в цифру - предст. с плав. точкой 
'''
# Example:
# Uo = R16*Uerr/(R16+R10) = 10*500/(10+5.11) = 330.907 mV
# 2^10 - 5000 mV
# x - Uo ; x = 67.76 ue = 68 ue = 0x44 ue
def calcCoeffTransf( value, channal, plot_cb ):
	# Получаем описание канала и кривой сенсора
	multer = channal.getSplitter()
	toDigital = channal.toBitCoeff()
	
	# Обработка
	U = channal.sensor_curve( I )
	
	# Умножаем на коэфф. перед. аналоговой цепи и "оцифровываем"
	Uadc = U * multer * toDigital	
	Udig = int( Uadc )
	
	# переводим в плавающую точку
	nprintValue( 'Udac, mV', U )
	nprintValue( 'Udig, ue', Udig )
	eprint( 'Code WORD: '+tc.byte4strhex( Udig )+'\n' )
	return Udig


# Run 
if __name__ == '__main__':
	# расчет коэффициентов трансформации
	listOfCurrents = [0]
	for I in listOfCurrents :
		msg = '\nI,A : ' + str( I ) + '\n'
		wprint( msg )
		Udig = calcCoeffTransf( I, metroChannal, None ) 
		
		# Записать в файл шаблон
		sets = { 'name': 'threshes.h', 'howOpen': 'w', 'coding': 'cp1251'}
		lstForWrite = list('')
		lstForWrite.append('\t#define CURRENT_THRESHOLD '+tc.byte4strhex( Udig )+"\t;"+str(I)+" A"+"\n")
		iow.list2file( sets=sets, lst=lstForWrite )
	'''	
	# смещение нуля при обратоной обработке
	I = 0
	Udig = calcCoeffTransf( I ) 
	# Записать в файл шаблон
	sets = { 'name': 'threshes.h', 'howOpen': 'a', 'coding': 'cp1251'}
	lstForWrite = list('')
	lstForWrite.append('#ifdef HALL_SENSOR')
	lstForWrite.append('\t#define ZERO_HALL_CORRECT '+tc.byte4strhex( Udig )+"\t;"+str(I)+" A"+"")
	lstForWrite.append('#endif ;HALL_SENSOR')
	iow.list2file( sets=sets, lst=lstForWrite )'''

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
