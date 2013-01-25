#-*- coding: utf-8 -*-
import sys
import math

# Other
import convertors_simple_data_types.xintyy_type_convertors as tc
import convertors_simple_data_types.float32_convertors as f32conv
from py_dbg_toolkit.doColoredConsole import co
import uasio.os_io.io_wrapper as iow

_kSets = { 'name': 'convertion.log', 'howOpen': 'a', 'coding': 'cp1251'}
_kOutProportion = 4000/4.6    # ue/V число, загружаемое в ЦАП 

# shortcuts
_nprint = co.printN
_wprint = co.printW
_eprint = co.printE

def _print_formatter(string):
    string = '0x'+string
    return string[:-1].replace(' ', ', 0x')

""" 
    Метод отображения результатов и плагины для вывода на комм. строку
    
    notes. : Низший модуль передает полностью всю информацию. Потом можно разбить
      регулярными выражениями

    rem. : функции обратного вызова можно собрать в кортеж и внизу управлять 
      действиями по имени
"""
# подборка плагинов
def plot_plugin(string):    # пустой
    None
    
def plot_plugin_full(string):
    print string
_kPluginList = {"None" : plot_plugin, 'Full':plot_plugin_full}

def _plot_item(msg, value):
    print msg+" "+str(value)
    ieee, mchip = f32conv.float_to_hex32(value, _kPluginList["None"])
    mchip = _print_formatter(mchip)
    
    lst = list()
    lst.append(';    '+msg+' '+mchip+'\n')
    iow.list2file(_kSets, lst)
    
def _print_string(msg):
    lst = list()
    lst.append(';    '+msg+'\n')
    iow.list2file(_kSets, lst)


def _plot_word(msg, word):
    """ msg : Lhl Hhl"""
    
    string = tc.byte2hex(int(word)%256)     # L
    string += ' '+ tc.byte2hex(int(word)/256)    # H
    print msg+' '+string

    lst = list()
    lst.append(';    '+msg+' '+string+'\n')
    iow.list2file(_kSets, lst)
    
def _new_line():
    lst = list()
    lst.append('\n')
    iow.list2file(_kSets, lst)

def _eprint_value(name, value):
    _eprint(name+' : '+str(value)+'\n')
def _wprint_value(name, value):
    _wprint(name+' : '+str(value)+'\n')
def _nprint_value(name, value):
    _nprint(name+' : '+str(value)+'\n')

def _hex_word_to_int(hexWord):
    sum = 0
    for pos in range(0, len(hexWord)):
        oneIt =  tc.hex2int(hexWord[ pos ])*math.pow(16, len(hexWord)-pos-1)
        sum += oneIt
    return sum

def calc_for_ukv(
        correcting_mult,  # температурный коэффициент, V/oC
        T,  # Температура 8 бит бит/градус
        src_shift_code  # значение кода для установки смещения по умолчанию из EEPROM
        ):
    """ Расчет для УКВ ЧМ
        @version : 1.0
        
        @notes:
            v 1.0
              precond.:
                1. попр. коэфф. всегда берется по модулю
                2. при коррекции кода склад. или выч. в зависимости от знака коэфф. коррекции
              contraints :
                
        @math:
            u_shift = u_shift_src+K*T    [float32]
            u_shift_code = to_code*(from_code*u_shift_src_code+K*T) = 
                u_shift_src+to_code*(K*T) = u_shift_src + int(T*(to_code*K)) = 
                u_shift_src+sign(K)*int(T*(to_code*abs(K)))
    """

    # Run
    correcting_mult = math.fabs(correcting_mult)    # ufloat
    # поправка
    K = correcting_mult*_kOutProportion    # ue(uint16)/oC положительная!
    dU = K*T    # dU ue(uint16)

    # значение изначального кода смещения для расчетов
    src_shift_code = _hex_word_to_int(src_shift_code)

    # uintXX = uintXX+(or -)uintXX
    out_shift_code = src_shift_code+math.copysign(1, correcting_mult)*dU    # вычитание вот здесь!
    
    # Report
    msg = 'T oC :'
    _plot_word(msg, T)
    _plot_item(msg, T)
    
    msg = 'K, ue(uint16)/oC:'
    _print_string(msg+' '+str(K))
    _plot_item(msg, K)
    
    msg = 'dU, ue LH:'
    _plot_word(msg, dU)
    msg = 'dU, ue :'
    _plot_item(msg, dU)
    msg = 'Out shift value, ue LH:'
    _plot_word(msg, out_shift_code)
    msg = 'Out shift value, ue float32:'
    _plot_item(msg, out_shift_code)
    _new_line()

if __name__=='__main__' :
    calc_for_ukv()


