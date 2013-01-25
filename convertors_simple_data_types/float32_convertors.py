#!/usr/bin/python
#-*- coding: utf-8 -*-
# import strFloatToBitArrPresent

import math as m
import xintyy_type_convertors as xint_module

 
def hexstr2float(src):
    """ seee_eeee emmm_mmmm mmmm_mmmm mmmm_mmmm    - �� ��������� """   
    srcList = src.split(' ')
    intList = list('')
    for i in srcList:
        for j in i:
            intList.append(hex2int(j))
            
    # � ��������� �������������� ������
    expExtr =  intList[2]+intList[1]*16+intList[0]*16*16
    expExtr = expExtr >> 3
    expExtr = expExtr & 255
    # ��������
    mant = intList[-1]+intList[-2]*16+intList[-3]*16*16+\
        intList[-4]*16*16*16+\
        intList[-5]*16*16*16*16+(intList[-6]&7)*16*16*16*16*16
    mant = float(mant)/m.pow(2, 23)+1  # ���������� � �������
    summaryo = mant*m.pow(2, (expExtr-127))
    if intList[0] >= 9:
        summaryo = -summaryo
    return summaryo

def hexMCHIPfloat32toFloat(src):
    """ ������� �������������� float MICROCHIP 32 to IEEE float32
        seee_eeee emmm_mmmm mmmm_mmmm mmmm_mmmm    - �� ���������
        0    1    2    3    -4   -3   -2   -1
        eeee_eeee smmm_mmmm mmmm_mmmm mmmm_mmmm - �������������� ������
    """
    srcList = src.split(' ')
    intList = list('')
    for i in srcList:
        for j in i:
            intList.append(xint_module.hex2int(j))
            
    # � ��������� �������������� ������
    # �������� ����������
    expExtr =  intList[1]+intList[0]*16

    # ��������
    mant = intList[-1]+\
        intList[-2]*16+\
        intList[-3]*256+\
        intList[-4]*16*256+\
        intList[-5]*256*256+\
        (intList[-6]&7)*16*256*256
    
    mant = float(mant)/m.pow(2, 23)+1  # ���������� � �������
    result = mant*m.pow(2, (expExtr-127))
    if intList[-6]&8 != 0:
        result = -result
    return result
    
def hex_mchip_float_to_float(src_string):
    """ 0xXX 0xYY 0xRR 0xVV """
    src_string = src_string.replace('0x','')
    src_string = src_string.replace(',','')
    return hexMCHIPfloat32toFloat(src_string)
    
    
def float_to_hex32(float_value, plot_callback):
    """ """
    abs_in_value = abs(float_value)
    # �������� ����������
    count_steps = 23+1

    # ����� ���������� �������
    begin = 0
    while 1:
        power = m.pow(2, begin)
        if abs_in_value-int(power) < 0:
            begin -= 1     # ����� ������
            break
    
        # ������� ������
        begin += 1
    
    # ������� �������������
    if abs_in_value < 1:
        begin = 0    # ����� ������ ������ ����

    # ������������ � ��o����� ����
    res = 0
    summary = ''
    for i in range(count_steps):
        # ����������� ����� ��������
        res = abs_in_value/m.pow(2, begin-i)
        
        # �������� ������� � ����
        if res < 1 :
            summary += '0'
        else :
            summary += '1'
            abs_in_value = abs_in_value-int(res)*m.pow(2, begin-i)
            
        # ������ �������
        if m.pow(2, begin-i) == 1:
            summary += ','
            
    # zero - ok
    #print summary
    
    # ����� ������ ����������, ���� ��� ������� � ������ 1
    first_one = summary.find('1')
    coma = summary.find(',')
    exp = 0
    if first_one != -1: # ������ ���
        if coma < first_one:
            exp = coma-first_one
        else :
            exp = coma-first_one-1
    else:
        exp = -127
    
    # �������� ����������
    exp += 127    # ������ �������� 
    
    exp = xint_module.char2bitarray(exp)

    # �������� ������������
    # ������ ���� �����
    if str(float_value)[0] == '-' :
        exp = '1'+exp
    else :
        exp = '0'+exp

    # ����������� ��������
    summary = summary.replace(',','')
    position_firs_one = summary.find('1')
    value_mant_in_str = summary[position_firs_one+1: -1]
    len_value_mant_in_str = len(value_mant_in_str)
    for j in range(23-len_value_mant_in_str):
        value_mant_in_str += '0'

    # ����� �������� � �������
    summary = exp+value_mant_in_str

    # �����������
    summary_tmp = '0000000'+summary+'0'
    float32 = ''
    for k in range(32+4+4):
        float32 += summary_tmp[k]
        if((k+1)%4 == 0):
            float32 += ' '
    aux_format_result = float32

    float32=''
    for k in range(32):
        float32 += summary[k]
        if((k+1)%4 == 0):
            float32 += ' '
    
    # ������ ���������
    ieee = float32

    # �������������� ����� ��� pic
    pure_exp = aux_format_result.split(' ')
    pure_exp = pure_exp[2]+' '+pure_exp[3]
    sign = ieee[0][0]
    
    # ��������� ��� ���
    mplab_float = ieee.split(' ')  # seee0_eeee1 e
    mplab_format = pure_exp
    tmp = '' 
    for i in mplab_float[3:]:
        tmp = tmp+' '+i
        
    # ������ ���������
    mplab_format = mplab_format + ' '+sign+mplab_float[2][1:]+tmp
    
    # �������� � ����� �����������
    if plot_callback:
        plot_callback( "IEEE : "+str(float_value) + 
            ' : '+xint_module.bit_formatted_array_to_hex(ieee)+' -> '+ieee)
        plot_callback( "MICROCHIP : "+str(float_value) + 
            ' : '+xint_module.bit_formatted_array_to_hex(mplab_format)+' -> '+mplab_format)
     
    return xint_module.bit_formatted_array_to_hex(ieee), xint_module.bit_formatted_array_to_hex(mplab_format)
    
#if name


