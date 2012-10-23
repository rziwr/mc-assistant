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

# ��������� ADDAC
dVmax = 430.0	# mV ����� ���
VmaxIdeal = 5000.0
Vmax = VmaxIdeal-dVmax 	# mV - ��� ������������ �������� ��� - �������� ��� ���. ����.
Vmax = VmaxIdeal 
capacity = 12

# ��������� ������� ������
Kiu = 188.0		# mV/A
dU = 500.0		# mV

# Deprecated
Resol = math.pow(2, capacity)
toDigital = Resol/Vmax#/VmaxIdeal
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
