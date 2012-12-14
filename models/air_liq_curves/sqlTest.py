#-*- coding: utf-8 -*-
# хранилище
import sqlite3


# Run
if __name__ == '__main__':
	conn = sqlite3.connect('Curves.db')
	
	# создаем курсор
	c = conn.cursor()

	# Create table
	c.execute('''
		CREATE TABLE if not exists stocks(
			NameCurve text primary key, 
			CurveValue text,
			Type boolean
		)'''
	)
	
	# запись в базу данных
	CurvesSet = {}
	hex = {}
	
	# конкретные кривые
	name = 'CurveSpeeds'
	hex[name] = False
	CurvesSet[name] = """	
	db	  1,12,   2,12,   3,12,   4,12,   5,12,   6,12,   7,12,   8,12,   9,12,  10,12,  11,12,  12,12,  13,12,   14,12,  15,12,  16,12,  17,12,  18,12,  19,12,   20,12
	db	 21,12,  22,12,  23,12,  24,12,  25,12,  26,12,  27,12,  28,12,  29,12,  30,12,  31,12,  32,12,  33,12,   34,12,  35,12,  36,12,  37,12,  38,12,  39,12,   40,12
	db	 41,12,  42,12,  43,12,  44,12,  45,12,  46,12,  47,12,  48,12,  49,12,  50,17,  51,22,  52,27,  53,32,   54,37,  55,42,  56,47,  57,52,  58,57,  59,62,   60,67
	db	 61,72,  62,77,  63,82,  64,87,  65,92,  66,97, 67,102, 68,107, 69,112, 70,117, 71,122, 72,127, 73,132,  74,137, 75,142, 76,147, 77,152, 78,157, 79,164,  80,164
	db	81,164, 82,164, 83,164, 84,164, 85,164, 86,164, 87,164, 88,164, 89,164, 90,164, 91,164, 92,164, 93,164,  94,164, 95,164, 96,164, 97,164, 98,164, 99,164, 	0x00
		"""
	name = 'CurveSpeeds2'
	hex[name] = False
	CurvesSet[name] = """
	db	  1,37,   2,37,   3,37,   4,37,   5,37,   6,37,   7,37,   8,37,   9,37,  10,37,  11,37,  12,37,  13,37,   14,37,  15,37,  16,37,  17,37,  18,37,  19,37,   20,37
	db	 21,37,  22,37,  23,37,  24,37,  25,37,  26,41,  27,45,  28,49,  29,52,  30,56,  31,60,  32,64,  33,67,   34,71,  35,75,  36,79,  37,82,  38,86,  39,90,   40,94
	db	 41,97,  42,101,  43,105,  44,109,  45,113,  46,113,  47,113,  48,113,  49,113,  50,113,  51,113,  52,113,  53,113,   54,113,  55,113,  56,113,  57,113,  58,113,  59,113,   60,113
	db	 61,113,  62,113,  63,113,  64,113,  65,113,  66,113, 67,113, 68,113, 69,113, 70,113, 71,113, 72,113, 73,113,  74,113, 75,113, 76,113, 77,113, 78,113, 79,113,  80,113
	db	81,113, 82,113, 83,113, 84,113, 85,113, 86,113, 87,113, 88,113, 89,113, 90,113, 91,113, 92,113, 93,113,  94,113, 95,113, 96,113, 97,113, 98,113, 99,113, 	0x00
		"""
	name = 'CurveSpeeds3'
	hex[name] = False
	CurvesSet[name] = """
	db	1,88,	2,88,	3,88,	4,88,	5,88,	6,88,   7,88,   8,88,   9,88,  10,88,  11,88,  12,88,  13,88,   14,88,  15,88,  16,88,  17,88,  18,88,  19,88,   20,88
	db	21,89,	22,91,	23,92,	24,94,	25,95,	26,97,  27,98,  28,100,  29,101,  30,103,  31,104,  32,106,  33,107,   34,109,  35,110,  36,112,  37,113,  38,115,  39,116,   40,118
	db	41,119,	42,121,	43,122,	44,124,	45,125,	46,127,  47,128,  48,130,  49,131,  50,133,  51,134,  52,136,  53,137,   54,139,  55,141,  56,142,  57,144,  58,145,  59,147,   60,148
	db	61,150,	62,151,	63,153,	64,154,	65,156,	66,157, 67,159, 68,160, 69,162, 70,164, 71,164, 72,164, 73,164,  74,164, 75,164, 76,164, 77,164, 78,164, 79,164,  80,164
	db	81,164,	82,164,	83,164,	84,164,	85,164,	86,164, 87,164, 88,164, 89,164, 90,164, 91,164, 92,164, 93,164,  94,164, 95,164, 96,164, 97,164, 98,164, 99,164, 	0x00
		"""
	name = 'CurveSpeeds4'
	hex[name] = False
	CurvesSet[name] = """
	db	  1,88,   2,88,   3,88,   4,88,   5,88,   6,88,   7,88,   8,88,   9,88,  10,88,  11,88,  12,88,  13,88,   14,88,  15,88,  16,88,  17,88,  18,88,  19,88,   20,88
	db	 21,88,  22,88,  23,88,  24,88,  25,88,  26,89,  27,90,  28,91,  29,93,  30,94,  31,95,  32,96,  33,97,   34,99,  35,100,  36,101,  37,102,  38,103,  39,105,   40,106
	db	 41,107,  42,108,  43,109,  44,111,  45,113,  46,113,  47,113,  48,113,  49,113,  50,113,  51,113,  52,113,  53,113,   54,113,  55,113,  56,113,  57,113,  58,113,  59,113,   60,113
	db	 61,113,  62,113,  63,113,  64,113,  65,113,  66,113, 67,113, 68,113, 69,113, 70,113, 71,113, 72,113, 73,113,  74,113, 75,113, 76,113, 77,113, 78,113, 79,113,  80,113
	db	81,113, 82,113, 83,113, 84,113, 85,113, 86,113, 87,113, 88,113, 89,113, 90,113, 91,113, 92,113, 93,113,  94,113, 95,113, 96,113, 97,113, 98,113, 99,113, 	0x00
		"""
	name = 'VIRTUAL_ONE'
	hex[name] = True
	CurvesSet[name] = """
	db 0x01, 0x33, 0x02, 0x33,  0x03, 0x33, 0x04, 0x33,  0x05, 0x33, 0x06, 0x33
	db 0x07, 0x33, 0x08, 0x33,  0x09, 0x33, 0x0A, 0x33,  0x0B, 0x33, 0x0C, 0x33
	db 0x0D, 0x33, 0x0E, 0x33,  0x0F, 0x33, 0x10, 0x33,  0x11, 0x33, 0x12, 0x33
	db 0x13, 0x33, 0x14, 0x33,  0x15, 0x39, 0x16, 0x3F,  0x17, 0x46, 0x18, 0x4C
	db 0x19, 0x52, 0x1A, 0x59,  0x1B, 0x5F, 0x1C, 0x66,  0x1D, 0x6C, 0x1E, 0x72
	db 0x1F, 0x7A, 0x20, 0x82,  0x21, 0x89, 0x22, 0x91,  0x23, 0x99, 0x24, 0xA0
	db 0x25, 0xA8, 0x26, 0xAF,  0x27, 0xB7, 0x28, 0xBF,  0x29, 0xBF, 0x2A, 0xBF
	db 0x2B, 0xBF, 0x2C, 0xBF,  0x2D, 0xBF, 0x2E, 0xBF,  0x2F, 0xBF, 0x30, 0xBF
	db 0x31, 0xBF, 0x32, 0xBF,  0x33, 0xBF, 0x34, 0xBF,  0x35, 0xBF, 0x36, 0xBF
	db 0x37, 0xBF, 0x38, 0xBF,  0x39, 0xBF, 0x3A, 0xBF,  0x3B, 0xBF, 0x3C, 0xBF
	db 0x3D, 0xBF, 0x3E, 0xBF,  0x3F, 0xBF, 0x40, 0xBF,  0x41, 0xBF, 0x42, 0xBF
	db 0x43, 0xBF, 0x44, 0xBF,  0x45, 0xBF, 0x46, 0xBF,  0x47, 0xBF, 0x48, 0xBF
	db 0x49, 0xBF, 0x4A, 0xBF,  0x4B, 0xBF, 0x4C, 0xBF,  0x4D, 0xBF, 0x4E, 0xBF
	db 0x4F, 0xBF, 0x50, 0xBF,  0x51, 0xBF, 0x52, 0xBF,  0x53, 0xBF, 0x54, 0xBF
	db 0x55, 0xBF, 0x56, 0xFE,  0x57, 0xFE, 0x58, 0xFE,  0x59, 0xFE, 0x5A, 0xFE
	db 0x5B, 0xFE, 0x5C, 0xFE,  0x5D, 0xFE, 0x5E, 0xFE,  0x5F, 0xFE, 0x60, 0xFE
	db 0x61, 0xFE, 0x62, 0xFE,  0x63, 0xFE, 0x00
		"""
	# Собираем набор имен
	
	# Insert a row of data
	INSET_REQ = 'INSERT INTO stocks VALUES ('
	fullReq = INSET_REQ+" '"+name+"','"+ CurvesSet[name] +" ',"+str(int(hex[name]))+")"
	try:
		c.execute( fullReq )
	except sqlite3.IntegrityError:
		print "Exist"
		# закрываем базу
		#c.close()
		#return None

	# Save (commit) the changes
	conn.commit()
	
	# Выворачиваем всю базу
	#for row in c.execute('SELECT NameCurve FROM stocks ORDER BY id'):
	for row in c.execute("SELECT * FROM stocks"):# WHERE  NameCurve = 'VIRTUAL_ONE_0'"):
		print row

	# We can also close the cursor if we are done with it
	c.close()
	#return None 