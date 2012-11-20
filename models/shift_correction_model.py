#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
sys.path.append( 'D:/home/lugansky-igor/pyPkgs/text-processors/pkgs' )
import math

import convertors_simple_data_types.IntTypeConvertors as tc
import convertors_simple_data_types.Float32Convertors as f32_conv

from py_dbg_toolkit.doColoredConsole import co
nprint = co.printN
wprint = co.printW
eprint = co.printE

import usaio.io_wrapper as iow
sets = { 'name': 'convertion.log', 'howOpen': 'a', 'coding': 'cp1251'}

''' '''
def printFormatter( string ):
	string = '0x'+string
	return string[:-1].replace( ' ', ', 0x' )

''' 
	Метод отображения результатов и плагины для вывода на комм. строку
	
	notes. : Низший модуль передает полностью всю информацию. Потом можно разбить
	  регулярными выражениями

	rem. : функции обратного вызова можно собрать в кортеж и внизу управлять 
	  действиями по имени
'''
# подборка плагинов
def plotPlugin( string ):	# пустой
	None
def plotPluginFull( string ):
	print string
	
pluginList = {"None" : plotPlugin, 'Full':plotPluginFull}
def plot( msg, value ):
	print msg+" "+str( value )
	ieee, mchip = f32_conv.run( value, pluginList["None"] )
	mchip = printFormatter( mchip )
	
	lst = list( )
	lst.append( msg+' '+mchip+'\n' )
	iow.list2file( sets, lst )

''' msg : Lhl Hhl'''
def plotWord( msg, word ):
	string = f32_conv.byte2hex( int( word )%256 ) 	# L
	string += ' '+ f32_conv.byte2hex( int( word )/256 )	# H
	print msg+' '+string

	lst = list( )
	lst.append( msg+' '+string+'\n' )
	iow.list2file( sets, lst )
	
def new_line( ):
	lst = list( )
	lst.append( '\n' )
	iow.list2file( sets, lst )

def eprintValue( name, value ):
	eprint( name+' : '+str( value )+'\n' )
def wprintValue( name, value ):
	wprint( name+' : '+str( value )+'\n' )
def nprintValue( name, value ):
	nprint( name+' : '+str( value )+'\n' )

def hexWordToInt( hexWord ):
	sum = 0
	for pos in range( 0, len( hexWord ) ):
		oneIt =  tc.hex2int( hexWord[ pos ] )*math.pow( 16, len( hexWord )-pos-1 )
		sum += oneIt
	return sum

''' 
	version : 1.0
	
	notes:
		v 1.0
		  precond.:
		    1. попр. коэфф. всегда берется по модулю
			2. при коррекции кода склад. или выч. в зависимости от знака коэфф. коррекции
		  contraints :
		    
	math:
		u_shift = u_shift_src+K*T	[float32]
		u_shift_code = to_code*(from_code*u_shift_src_code+K*T) = 
			u_shift_src+to_code*(K*T) = u_shift_src + int(T*(to_code*K)) = 
			u_shift_src+sign(K)*int(T*(to_code*abs(K)))
'''
# Расчет для УКВ ЧМ
T = 10	# Температура 8 бит бит/градус
src_shift_code = '0FFF'	# значение кода для установки смещения по умолчанию из EEPROM

# температурный коэффициент
corrected_mult = -4.9 * 5 * 1e-3	# V/oC
corrected_mult = math.fabs( corrected_mult )	# ufloat

# поправка
out_proportion = 4000 / 4.6	# ue/V число, загружаемое в ЦАП 
mult = corrected_mult * out_proportion	# V/oC положительная!
dU = mult * T	# deltaU V uintXX

# значение изначального кода смещения для расчетов
src_shift_code = hexWordToInt( src_shift_code )

# uintXX = uintXX+( or - )uintXX
out_shift_code = src_shift_code+math.copysign( 1, corrected_mult )*dU	# вычитание вот здесь!

# Report
msg = 'T oC :'
plot( msg, T )
msg = 'mult, V/oC :'
plot( msg, mult )
msg = 'deltaU, ue LH:'
plotWord( msg, dU )
msg = 'deltaU, ue :'
plot( msg, dU )
msg = 'Out shift value, ue LH:'
plotWord( msg, out_shift_code )
msg = 'Out shift value, ue float32:'
plot( msg, out_shift_code )
new_line( )

''' Trash
def intWordToHex( intWord ):
	sum = ''
	
def shift2Code( fShift ):
	Usm_needed = fShift

	# 2. Переводим в код
	V_test = 1.433	# V - на транзисторе при коде 0xFFF
	V_test_code = '0FFF'
	V_test_code = hexWordToInt( V_test_code ) # вид для расчета
	K_V2code = V_test_code / V_test
	Code =K_V2code * Usm_needed
	
	# Report
	co.printE( 'U : ' + str( Usm_needed )+'\n' ) 
	co.printW( 'Code : ' + str( int( Code ) )+'\n' )
	msg = 'Hex code, LH: : '
	plotWord( msg, Code )
	
	# Выходные параметры
	return Code

# Перобразование смещения
T = 26.0	# Температура 8 бит бит/градус

# температурный коэффициент
corrected_mult = 4.9 * 5 * 1e-3	# V/oC

# расчет
dUsm = T * corrected_mult

# В виде кода
dUsm_code = shift2Code( dUsm )
K_oC2Code = dUsm_code / T
# переводим в плавающую точку
msg = 'T to code, float32:'
plot( msg, K_oC2Code )
co.printW( 'T to code : '+str( K_oC2Code )+'\n' )

# нулевое приближение в коде
#U = 1.433
#U_code = shift2Code( U )'''



