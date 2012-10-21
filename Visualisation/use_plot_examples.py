#-*- coding: utf-8 -*-
# View
from matplotlib import pyplot
import pylab

# Calc engines
from scipy.interpolate import interp1d
import random
import numpy
''' hist '''
def histPlt():
	x = [random.gauss(3,1) for _ in range(400)]
	y = [random.gauss(4,2) for _ in range(400)]

	bins = numpy.linspace(-10, 10, 100)

	pyplot.hist(x, bins, alpha=0.5)
	pyplot.hist(y, bins, alpha=0.5)
	pyplot.show()
	
''' linear interp. '''
def linInterpol():
	# входные данные
	y = [20, 20, 45, 75, 75, 100, 100]	# %
	x = [1, 20, 30, 40, 85, 86, 99]
	
	# Линейная
	f = interp1d(x, y)
	
	# Кубическая
	f2 = interp1d(x, y, kind='cubic')
	
	# Новая ось
	xnew = numpy.linspace(1, x[-1], x[-1])
	#pyplot.plot(x,y,'o',xnew,f(xnew),'v-', xnew, f2(xnew),'--')
	pyplot.plot(x,y,'o',xnew,f(xnew),'v-')
	pyplot.legend(['data', 'linear', 'cubic'], loc='best')
	pyplot.grid(True)
	pyplot.show()