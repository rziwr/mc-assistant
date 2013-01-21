#!/usr/bin/python
#-*- coding: utf-8 -*-
# import ui
import sys
sys.path.append('D:/home/lugansky-igor/libs-dev/py-reuse-pkgs')
import convertors_simple_data_types.float32_convertors as f32cnv
import usaio.io_wrapper as io_w
'''import api_os_wrappers.os_wrapper as os_w'''
def _get_consts_set(partial_name, value, rpt_list, len_line):
    rpt_list.append('    ; Value : '+str(value))
    ieee, mchip = f32cnv.float_to_hex32(value, None)
    
    mchip = mchip.split(' ')
    mchip = ', 0x'.join(mchip)
    mchip = '0x'+mchip[:-4]
    
    list_const = mchip.split(' ')
    
    # пишем в заголовочный файл
    i = 0
    for at in list_const:
        rpt_list.append('    #define '+
            partial_name+str(i)+' '+
            at.replace(',', ''))
        i += 1
    
    rpt_list.append('    ; Mchip format : '+mchip)
    rpt_list.append('    #define _kLenFIRLine '+str(len_line))
    
if __name__=='__main__':
    rpt_list = list()
    # максимальная ошибка 10*lenFirLine градусов
    # 0x018d(397) 0x0fff(4095)
    low = 397   # 0.4 V
    low_value_V = 0.4
    work_value = 1.2    # V
    
    hight = low*work_value/low_value_V
    delta = hight-low
    
    # максимальная ошибка
    max_temp_err = 10.0   # oC
    len_FIR_line = 20    # число отсчетов для пониженной точности
    max_err = max_temp_err*len_FIR_line
    
    value = delta/max_err
    rpt_list.append('#ifdef HIGH_TERMO_RESOLUTION')
    _get_consts_set('_kRefARU', value*2, rpt_list, len_FIR_line/2)
    rpt_list.append('#else')
    _get_consts_set('_kRefARU', value*2, rpt_list, len_FIR_line)
    rpt_list.append('#endif  ; HIGH_TERMO_RESOLUTION')
    '''i = 0
    macro_name = '    _mDspFillMathTmp '
    for at in list_const:
        rpt_list.append('#define _kRefARU'+str(i)+' '+at.replace(',', ''))
        macro_name += '_kRefARU'+str(i)+','
        i += 1
    rpt_list.append(macro_name[:-1])'''
    
    # Rpt
    settings = {'name':'aru_calc_rpt.txt', 'howOpen':'w', 'coding':'cp1251'}
    io_w.list2file(settings, rpt_list)
    #print f32cnv.hex_mchip_float_to_float("0x84, 0x00, 0x00, 0x00")
    print 'Done'