#-*- coding: utf-8 -*-
import sys
sys.path.append('D:/home/lugansky-igor/github-dev/py-bale')
sys.path.append('D:/home/lugansky-igor/github-dev')
import json

# dev
import uasio.os_io.io_wrapper as iow
from py_dbg_toolkit.doColoredConsole import co
import convertors_simple_data_types.xintyy_type_convertors as tc

# App
import _sensors_uni as app_reuse_code

nprint = co.printN
wprint = co.printW
eprint = co.printE
def eprintValue( name, value ):
    eprint( name+' : '+str(value)+'\n')
def wprintValue( name, value ):
    wprint( name+' : '+str(value)+'\n')
def nprintValue( name, value ):
    nprint( name+' : '+str(value)+'\n')

def _init_sensors():
        # читае конфигурация сенсора
    sensor_sets = app_reuse_code.get_sensor_cfg('I')

    # Настройки прочитаны, можно разбирать их
    value2voltage = app_reuse_code.value2voltageHall
    SensorChannal = app_reuse_code.SensorChannalHall

    metro_channal = SensorChannal( sensor_sets,'adc_metro','splitter_metro_parems', value2voltage )
    threshold_channal = SensorChannal( sensor_sets,'dac_threshes','splitter_threshold_parems', value2voltage )
    return metro_channal, threshold_channal
    
def main(list_of_currents):
    metro_channal, threshold_channal = _init_sensors()
    
    # смещение нуля при обратной обработке
    I = 0
    Udig_zero, capacity = app_reuse_code.calc_coeff_transform( I, metro_channal ) 
    # Записать в файл шаблон
    fname = 'threshes.h'
    sets = { 'name': fname, 'howOpen': 'w', 'coding': 'cp1251'}
    
    print 'Threshes write to file '+fname
    
    result_list = list('')
    result_list.append('#ifdef HALL_SENSORS')
    result_list.append('\t#define ZERO_HALL_CORRECT '+Udig_zero+"\t;"+
        str(I)+" A; bits - "+capacity+'\n' )
    iow.list2file( sets=sets, lst=result_list )
    
    # Пороги
    result_list = list('')
    # Записать в файл шаблон
    sets['howOpen'] = 'a'
    for I in list_of_currents :
        wprintValue('\nI,A : ', I)
        Udig, capacity = app_reuse_code.calc_coeff_transform( I, threshold_channal ) 
        eprintValue('U_code', Udig)
        result_list.append('\t#define CURRENT_THR '+Udig+"\t;"+
            str(I)+" A  bits - "+capacity)
            
    # Находим коэффициент пересчета
    
    """I = 10
    Udig_value, capacity = app_reuse_code.calc_coeff_transform( I, metro_channal ) 
    print Udig_value
    realCodeCurrent = tc.hex_word_to_uint(Udig_value)-tc.hex_word_to_uint(Udig_zero)
    k = I/realCodeCurrent
    wprintValue('K code to A :', k)
    
    result_list.append(';const double TA_CURRENT_MUL = '+str(k)+';')
"""
    # Закрываем запись
    result_list.append('#endif ;HALL_SENSOR\n')
    iow.list2file( sets=sets, lst=result_list )

# Run 
if __name__ == '__main__':
    main()
    

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
