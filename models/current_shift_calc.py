#-*- coding: utf-8 -*-
# core
import math
import json

# utils
import usaio.io_wrapper as iow
from pyDbg.doColoredConsole import co
import simpleDataTypesConvertors.Float32Convertors as f32cnv
import simpleDataTypesConvertors.IntTypeConvertors as tc

# ������ ������������ �������
sets = { 'name': 'current_sensor.cfg', 'howOpen': 'r', 'coding': 'cp1251'}
sensorSettings = iow.file2list( sets )

# here we are converting python object to json string
sensor_sets = json.loads( ' '.join(sensorSettings))
print json.dumps(sensor_sets, sort_keys=True, indent=2)

# ��������� �������� ����������
splitter_params = sensor_sets['splitter_params']
R1 = splitter_params['R1']
R2 = splitter_params['R2']

splitter = R2/(R1+R2)

# ��������� ADDAC
addac = sensor_sets['addac']
dVmax = addac[ 'dVmax' ]	# mV ����� ���
VmaxIdeal = addac[ 'VmaxIdeal' ]
capacity = addac[ 'capacity' ]

Vmax = VmaxIdeal-dVmax 	# mV - ��� ������������ �������� ��� - �������� ��� ���. ����.

# ��������� ������� ������
curve_params = sensor_sets['curve_params']
Kiu = curve_params[ 'Kiu' ]		# mV/A
dU = curve_params[ 'dU' ]		# mV

# Coeffs
resolution = math.pow(2, capacity)
toDigital = resolution/Vmax
toAnalog = 1/toDigital


''' ��� � ��� � ������� I, A '''
''' ��� �� ��������� � ����� - ������. � ����. ������ '''
def toDigitalFull( U, mult, toDigital ):
	Uadc = U * mult	# �� ����� �������� ������ ��� ������
	# ADC
	Udig = toDigital * Uadc
	return Udig
	
def calcCoeffTransf(I):
	# �������� ����������� �����������
	multer = 1	# ���� �������� � ������ �����
	U = I * Kiu + dU
	co.printW( 'Udac : ' + str( U )+'\n')
	Udig_f = toDigitalFull( U, multer, toDigital )
	Udig = int( Udig_f )
	
	# ������������ ��� - �������� �� Y
	Udig_noise_f = toDigitalFull( dU, multer, toDigital )
	
	# ��������� �������� - ��� ����
	Udig_corr = int(Udig_f - Udig_noise_f)	# ����������� ����� ����������

	# ����������� ��������. ��� ������ �������� ���� - ��� ��������� � �����������
	# Warning : ������� ���������� � ��������, �� �������� ������������, ������� 
	#   �������� ����� ��� ����
	Ktrans = I/Udig_corr  # A/ue
	
	# ��������� � ��������� �����
	print 'capacity : ' + str( capacity )
	co.printN( 'Udig_src, ue : ' )
	co.printE( tc.byte4strhex( Udig )+'\n')
	return Udig

''' ������ �������� '''
def printRpt( value, valueDisplacemented, valueScaled, valueCode, Kda ):
	print '\n<< Output values:'
	print 'Code : '+str(valueCode)
	print 'Kda : '+str(Kda)

# Run 
if __name__ == '__main__':
	# ������ ������������� �������������
	listOfCurrents = [15, 10, 5]
	for current in listOfCurrents :
		msg = '\nI,A : ' + str( current ) + '\n'
		co.printW( msg )
		print calcCoeffTransf( current ) 
