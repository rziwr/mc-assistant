#!/usr/bin/python
#-*- coding: utf-8 -*-
''' 
    file : testFloat32Conversion
'''
import float32_convertors as f32cnv
import unittest


def plotCallBack(string):
    pass


class TestFloatConversion(unittest.TestCase):
    def setUp(self):
        pass

    ''' '''

    def testInv(self):
        # проверим обр. преобр
        doubleOne = 1.0
        doubleOneFromMCHIP = f32cnv.hexMCHIPfloat32toFloat("7F 00 00 00")

        self.assertEqual(doubleOneFromMCHIP, doubleOne)

        # проверим обр. преобр
        doubleOne = 0.5
        doubleOneFromMCHIP = f32cnv.hexMCHIPfloat32toFloat("7E 00 00 00")

        self.assertEqual(doubleOneFromMCHIP, doubleOne)

    def testInvIEEEOneValue(self):
        self.assertEqual(f32cnv.hexstr2float("3F 80 00 00"), 1.0)

    def testInvMCHIPOneValue(self):
        self.assertEqual(f32cnv.hexMCHIPfloat32toFloat("7F 00 00 00"), 1.0)

    def testInvIEEETwoValue(self):
        self.assertEqual(f32cnv.hexstr2float("40 00 00 00"), 2.0)

    def testInvMCHIPTwoValue(self):
        self.assertEqual(f32cnv.hexMCHIPfloat32toFloat("80 00 00 00"), 2.0)

    def testIEEEOneValue(self):
        doubleOne = 1.0
        # проверка преобразования
        m, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, plotCallBack)
        self.assertEqual(f32cnv.hexstr2float(a), doubleOne)

    def testIEEETwoValue(self):
        doubleOne = 2.0
        # проверка преобразования
        m, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, plotCallBack)
        self.assertEqual(f32cnv.hexstr2float(a), doubleOne)

    def testIEEEHalfValue(self):
        doubleOne = 0.5
        # проверка преобразования
        m, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, plotCallBack)
        self.assertEqual(f32cnv.hexstr2float(a), doubleOne)

    ''' преобразование 1 и 2
        ошибка 1 = 0.5
    '''

    def testOneValue(self):
        doubleOne = 1.0
        # проверка преобразования
        m, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, plotCallBack)
        self.assertEqual(f32cnv.hexMCHIPfloat32toFloat(doubleOneDirectCnvMCHIP), doubleOne)

    ''' '''

    def testTwoValue(self):
        doubleOne = 2.0
        # проверка преобразования
        m, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, plotCallBack)
        self.assertEqual(f32cnv.hexMCHIPfloat32toFloat(doubleOneDirectCnvMCHIP), doubleOne)

    ''' '''

    def testHalfValue(self):
        doubleOne = 0.5
        # проверка преобразования
        message, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, plotCallBack)
        self.assertEqual(f32cnv.hexMCHIPfloat32toFloat(doubleOneDirectCnvMCHIP), doubleOne)

    ''' Просто тест на работоспособность '''

    def testSimple(self):
        # IEEE
        self.assertEqual(f32cnv.hexstr2float("43 1B A0 00"), 155.625)

        # MCHIP
        self.assertEqual(f32cnv.hexstr2float("43 1B A0 00"), 155.625)

    def testZero(self):
        doubleOne = 0.0
        # проверка преобразования
        m, a, doubleOneDirectCnvMCHIP = f32cnv.float_to_hex32(doubleOne, None)
        self.assertEqual(a[:-1], '00 00 00 00')

# Run tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFloatConversion)
    unittest.TextTestRunner(verbosity=2).run(suite)
