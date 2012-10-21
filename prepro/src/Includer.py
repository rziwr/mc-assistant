#-*- coding: utf-8 -*-
""" 
	abs. : обрабатывает include директивы
		на входе файл ansii(или и тот и тот)
		на выходе utf8
	file : import Includer
"""

# прочитать файл в список
# для всех элементов списка проверить есть ли include кл. слово
#   сохранить эту строку - потом возможно она будет целиком заменена сод. файла
# провертть нужно ли на ее место вкл
# Считать исх. файл и целевые в строк и в исх. прямо заменить 
# Пока всякие глупости не учитываю!!

# Проблемы
#   1. циклические записимости
#   2. закомментированные строки

import sys
from usaio.io_wrapper import *

""" Читаем файл в список """
def file2list( fname, coding ):
	listLines = list('')
	sets = { 'name' :  fname, 'howOpen' : 'r', 	'coding' : coding }
	file = FabricOpen( sets )
	if file != None:
		listLines = file.toList()
		return listLines
	else :
		return None
		
def file2ListLines( fname ):
	return file2list( fname, 'cp1251' )

""" Читаем как utf8 """
def file2ListLinesUnicode( fname ):
	return file2list( fname, 'utf_8' )

""" """
def insertFileContent( file, at ):
	# да действующая директива
	# Выделяем адрес файла включения
	at = at.split()
	atPath = at[1]
	atPath = atPath.replace('>','')	# можно в цикл свернуть!
	atPath = atPath.replace('<','')
	atPath = atPath.replace('/','\\')
	if atPath[0] != '.':
		atPath = '.'+atPath

	# Закомменчиваем что включили
	file.write(';'+atPath+'\n')
	
	# Получае содержимое вкл. файла
	linesFromInc = file2ListLines( atPath )
	print atPath
	
	# Лучше выделить новыми строками
	file.write( '\n' )
	
	
	# пишем в целевой файл
	if linesFromInc != None:
		for jat in linesFromInc:
			file.write( jat )
	
	# чтобы ошибки в стыковке файлов не было
	file.write( u'\n' )
""" """
def analyseContent( listLines, targetFname ):
	fixModuleNameYes = False
	occureInc = False
	sets = { 'name' :  targetFname, 'howOpen' : 'wb',  'coding' : 'utf_8' }
	file = FabricOpen( sets )
	
	# Проверяем есть ли файл для записи
	if file != None and listLines != None:
		for at in listLines:
			# есть ли директива включения
			if 'include' in at:
				# проверка незакомментированности
				if at[0] != ';':
					if not 'P18F8722.inc' in at:
						# вставлем содержимое файла
						insertFileContent( file, at )
							
						# Нашлись включения
						occureInc = True
			else :	# просто пишем в файл
				if 'THIS' in at:
					if not fixModuleNameYes:
						fixModuleNameYes = True
				file.write(at)
		file.write('\n')
	else:
		occureInc = False
	
	# выходим
	return occureInc 	# конец рекурсии

""" 
	abs. : assemble file 
	Warning! : циклические зависимости не обрабатывает
"""
def assembleCompileUnit( fname, targetFileName ):
	# Читаем исходный файл
	listLines = file2ListLines( fname )
	
	# Ищем директивы включения
	occureInd = True
	# файл пишется как юникод на первой итерации
	while analyseContent( listLines, targetFileName ):
		listLines = file2ListLinesUnicode( targetFileName )
	
	# если хотя бы один файл не найден ошибка и выходим!!





