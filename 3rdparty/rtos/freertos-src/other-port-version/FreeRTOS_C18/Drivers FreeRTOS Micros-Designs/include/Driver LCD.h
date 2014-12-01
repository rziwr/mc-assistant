/**
   \version: 1.0

   
   \author Suky (Casanova Alejandro) 
   \web www.micros-designs.com.ar
   \date 27/07/11


///////////////////////////////////////////////////////////////////////////
////                                                                   ////
////                                                                   ////
////        (C) Copyright 2010 www.micros-designs.com.ar               ////
//// Este código puede ser usado, modificado y distribuido libremente  ////
//// sin eliminar esta cabecera y  sin garantía de ningún tipo.        ////
////                                                                   ////
////                                                                   ////
/////////////////////////////////////////////////////////////////////////// 
   
 *- Version Log --------------------------------------------------------------*
 *   Fecha       Autor                Comentarios                             *
 *----------------------------------------------------------------------------*
 * 27/07/11      Suky               Original (Rev 1.0)                        *
 *----------------------------------------------------------------------------* 

 */ 

#ifndef __LCD_GENERIC_H_
#define __LCD_GENERIC_H_

#include <p18cxxx.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include "GenericTypeDefs.h"

/* ****************************************************************************************************** */
/* ** Para no utilizar el PIN RW comentar la siguiente definición ** */
#define LCD_USE_RW 
/* ** El siguiente modo no utiliza el PIN RW** */
//#define LCD_USE_3PINES		// Se utiliza registro de desplazamiento para DATA[0..3] y RS.
/* -------------------------------------------------------------------- */
/* **  DEFINICION PARA INICIALIZACION DEL LCD ** */
#define LcdType 2 			// 0=5x7, 1=5x10, 2=varias lineas
/* ** DEFINICION PARA TRABAJAR CON LCD DE 2 LINEAS o 4 LINEAS** */
#define LCD_4LINES
/* ** DEFINICIONES DE DIRECCIONAMIENTO DE LINEAS EN LCD ** */
#define LCD_LINE_1_ADDRESS 0x00
#define LCD_LINE_2_ADDRESS 0x40
#if defined(LCD_4LINES)
	#define LCD_LINE_3_ADDRESS 0x14
	#define LCD_LINE_4_ADDRESS 0x54
#endif
/* -------------------------------------------------------------------- */
#define LCD_COMMAND	0
#define LCD_DATA		1

#if defined(LCD_USE_3PINES) && defined(LCD_USE_RW)
	#undef LCD_USE_RW
#endif
/* ************************** MPLAB C18 **************************************** */
#if defined(__18CXX)
	#include <p18cxxx.h>
	
	#define __delay_1Cycle()	{Nop();}
	#define __delay_1us()		{Nop();Nop();Nop();Nop();Nop();Nop();Nop();Nop();Nop();Nop();Nop();Nop();}
  
	#define CONFIG_INPUT    1
	#define CONFIG_OUTPUT   0
	
	#ifndef LCD_USE_3PINES
		/* ** Pines tolerables a 5V para usar RW ** */
		#define LCD_DATA_PIN_7 				LATBbits.LATB7
		#define LCD_DATA_PIN_6 				LATBbits.LATB6
		#define LCD_DATA_PIN_5 				LATBbits.LATB5
		#define LCD_DATA_PIN_4 				LATBbits.LATB4
		
		#define LCD_READ_PIN_7				PORTBbits.RB7
		#define LCD_READ_PIN_6				PORTBbits.RB6
		#define LCD_READ_PIN_5				PORTBbits.RB5
		#define LCD_READ_PIN_4				PORTBbits.RB4
		
		
		#define LCD_TRIS_DATA_PIN_7      TRISBbits.TRISB7
		#define LCD_TRIS_DATA_PIN_6      TRISBbits.TRISB6
		#define LCD_TRIS_DATA_PIN_5      TRISBbits.TRISB5
		#define LCD_TRIS_DATA_PIN_4      TRISBbits.TRISB4
		
		
		#define LCD_E_PIN						LATBbits.LATB2 
		#define LCD_RS_PIN					LATBbits.LATB0 
		#ifdef LCD_USE_RW
			#define LCD_RW_PIN				LATBbits.LATB1 
		#endif
		
		#define LCD_TRIS_E					TRISBbits.TRISB2 
		#define LCD_TRIS_RS					TRISBbits.TRISB0  
		#ifdef LCD_USE_RW 
			#define LCD_TRIS_RW				TRISBbits.TRISB1 
		#endif 
	#else
		#define LCD_DATA_PIN  				LATBbits.LATB4
		#define LCD_CLOCK_PIN 				LATBbits.LATB5
		#define LCD_E_PIN	  					LATBbits.LATB6
	
		#define LCD_TRIS_DATA				TRISBbits.TRISB4
		#define LCD_TRIS_CLOCK				TRISBbits.TRISB5
		#define LCD_TRIS_E					TRISBbits.TRISB6
	#endif
#endif

UINT8 ui8BusyLCD(void);
void vWriteLCD(UINT8 Data,UINT8 Type);
void vInitLCD(void);
void vGotoxyLCD(UINT8 x,UINT8 y);
void vLCDPutc(UINT8 Data);

portCHAR cLCDPutc(UINT8 Data);
portCHAR cLCDPutrs(UINT8 x, UINT8 y, rom UINT8 *Data);
portCHAR cLCDPuts(UINT8 x, UINT8 y, UINT8 *Data);
portCHAR cGotoxyLCD(UINT8 x,UINT8 y);

typedef struct{
	UINT8	Data;
	UINT8 *PtrDataRam;
	rom UINT8 *PtrDataRom;
	UINT8 x;
	UINT8 y;
}LCDDATA;

typedef struct{
	UINT8 x;
	UINT8 y;
}LCDGOTO;

#endif