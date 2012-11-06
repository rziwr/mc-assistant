#!/usr/bin/python
#-*- coding: utf-8 -*-
import math

import ui

import simpleDataTypesConvertors.IntTypeConvertors as tc
import simpleDataTypesConvertors.Float32Convertors as f32_conv

from pyDbg.doColoredConsole import co
nprint = co.printN
wprint = co.printW
eprint = co.printE

import usaio.io_wrapper as iow

''' '''
def printFormatter(string):
	string = '0x'+string
	return string[:-1].replace(' ',', 0x')

''' 
	Метод отображения результатов и плагины для вывода на комм. строку
	
	notes. : Низший модуль передает полностью всю информацию. Потом можно разбить
	  регулярными выражениями

	rem. : функции обратного вызова можно собрать в кортеж и внизу управлять 
	  действиями по имени
'''
def plotPlugin(string):	# пустой
	None
def plotPluginFull(string):
	print string

sets = { 'name': 'convertion.log', 'howOpen': 'a', 'coding': 'cp1251'}
	
# подборка плагинов
pluginList = {"None" : plotPlugin, 'Full':plotPluginFull}
def plot(msg, value):
	print msg+" "+str(value)
	ieee, mchip = f32_conv.run(value, pluginList["Full"])
	mchip = printFormatter(mchip)
	
	lst = list()
	lst.append(msg+' '+mchip+'\n')
	iow.list2file( sets, lst )

''' msg : Lhl Hhl'''
def plotWord(msg, word):
	string = f32_conv.byte2hex(int(word)%256) 	# L
	string += ' '+ f32_conv.byte2hex(int(word)/256)	# H
	print msg+' '+string

	lst = list()
	lst.append(msg+' '+string+'\n')
	iow.list2file( sets, lst )
	
def rout():
	lst = list()
	lst.append('\n')
	iow.list2file( sets, lst )
	
''' ''' ''' '''

def eprintValue( name, value ):
	eprint( name+' : '+str(value)+'\n')
def wprintValue( name, value ):
	wprint( name+' : '+str(value)+'\n')
def nprintValue( name, value ):
	nprint( name+' : '+str(value)+'\n')

def hexWordToInt( hexWord ):
	sum = 0
	for pos in range( 0, len( hexWord ) ):
		oneIt =  tc.hex2int( hexWord[ pos ] )*math.pow( 16, len( hexWord )-pos-1 )
		sum += oneIt
	return sum
	
def intWordToHex( intWord ):
	sum = ''

# Расчет для УКВ ЧМ
T = 0	# Температура 8 бит бит/градус

# температурный коэффициент
corrected_mult = 4.9 * 5 * 1e-3	# V/oC

# поправка
mult = 4.9/1000*5*4000.0/4.6	# V/oC положительная!
delta_U = mult*T	# deltaU V

# конкретное значение смещения
hexWord = '0F99'
Usm_src = hexWordToInt( hexWord ) 
Usm_src -= delta_U	# вычитание вот здесь!

# Report
'''
msg = 'T oC :'
ui.plot(msg, T)
msg = 'mult V/oC :'
ui.plot(msg, mult)
msg = 'deltaU, ue LH:'
ui.plotWord(msg, delta_U)
msg = 'deltaU ue :'
ui.plot(msg, delta_U)
msg = 'Usm src, ue LH:'
ui.plotWord(msg, Usm_src)
msg = 'Usm src, ue float32:'
ui.plot(msg, Usm_src)
ui.rout()'''


''' '''
def shift2Code( fShift ):
	Usm_needed = fShift

	# 2. Переводим в код
	V_test = 1.433	# V - на транзисторе при коде 0xFFF
	V_test_code = '0FFF'
	V_test_code = hexWordToInt( V_test_code ) # вид для расчета
	K_V2code = V_test_code / V_test
	Code =K_V2code * Usm_needed
	
	# Report
	co.printE( 'U : ' + str( Usm_needed )+'\n') 
	co.printW( 'Code : ' + str( int(Code) )+'\n')
	msg = 'Hex code, LH: : '
	plotWord(msg, Code)
	
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
plot(msg, K_oC2Code)
co.printW( 'T to code : '+str(K_oC2Code)+'\n' )

# нулевое приближение в коде
#U = 1.433
#U_code = shift2Code( U )



