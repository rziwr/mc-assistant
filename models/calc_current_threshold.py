#-*- coding: utf-8 -*-
import simpleDataTypesConvertors.Float32Convertors as f32cnv
import simpleDataTypesConvertors.IntTypeConvertors as tc
import math
import ModelADDAC as adda
from pyDbg.doColoredConsole import co

# ������ ������������ �������
from current_head import *


''' ��� � ��� � ������� 
I, A
'''
''' ��� �� ��������� � ����� - ������. � ����. ������ '''
def toDigitalFull( U, mult, toDigital ):
	Uadc = U * mult	# �� ����� �������� ������ ��� ������
	# ADC
	Udig = toDigital * Uadc
	return Udig
	
def msgSplit(msg):
	result = ''
	for at in msg:
		result += "'"
		result += at
		result += "',"
	return result
	
#! ����� ��� �������� ! � ������� �� ��������� ��� ���������, ��� ����, �� ����!
def calcCoeffTransf(I):
	# �������� ����������� �����������
	#multer = Splitter	# � �������� �� ���
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

''' ������ �������� '''
def printRpt( value, valueDisplacemented, valueScaled, valueCode, Kda ):
	print '\n<< Output values:'
	print 'Code : '+str(valueCode)
	print 'Kda : '+str(Kda)

# Run 
if __name__ == '__main__':
	# ������ ������������� �������������
	listOfCurrents = [16]
	for current in listOfCurrents :
		msg = '\nI,A : ' + str( current ) + '\n'
		co.printW( msg )
		print calcCoeffTransf( current ) 
	
	# ���������
	'''valueDict = {}
	valueDict[ 'value' ] = I
	valueDict['displacement'] = dU
	valueDict['converter' ] = Kiu
	valueDict['scale'] = Splitter
	valueDict['capacity'] = capacity
	valueDict['Vmax'] = Vmax 
	code, Kda = adda.modelADC( valueDict, printRpt, adda.calcZeroDisplacmentY )'''





