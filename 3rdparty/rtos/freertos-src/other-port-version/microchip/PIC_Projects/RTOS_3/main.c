#include <p18cxxx.h>
#include <stdio.h>
#include <delays.h>
#include <usart.h>

#include "FreeRTOSConfig.h"
#include <FreeRTOS.h>
#include <task.h>
#include <list.h>
#include <semphr.h>
#include <alloc.h>
#include "serial.h"

#ifdef __18LF45K22
    #pragma config FCMEN = OFF
    #pragma config IESO = OFF
    #pragma config BOREN = OFF
    #pragma config LVP = OFF
    #pragma config XINST = ON
    #pragma config WDTEN = OFF
#endif

/* Constants required for the communications.  Only one character is ever 
transmitted. */
#define mainCOMMS_QUEUE_LENGTH			( 5 )
#define mainNO_BLOCK					( ( portTickType ) 0 )
#define mainBAUD_RATE					( ( unsigned long ) 9600 )
/* block a long time */
#define mainRX_BLOCK_TIME               ( ( portTickType) 0xffff )


long int i, j = 0;
xSemaphoreHandle xSem = NULL;

/* Handle to the com port used by both tasks. */
static xComPortHandle xPort = NULL;

/* We should find that each character can be queued for Tx immediately and we
don't have to block to send. */
#define comNO_BLOCK					( ( portTickType ) 0 )

void Task1(void *params) {
    signed char cByteToSend;
	__reclaim_stack();
	xSem = xSemaphoreCreateMutex();
	while(1) {		
		if(xSemaphoreTake(xSem, (portTickType) 10) == pdTRUE) {
			//puts("abcd");
            //putrs1USART("abcd\n\r");
            for( cByteToSend = 'A'; cByteToSend <= 'F'; cByteToSend++ )
		    {
			  if( xSerialPutChar( xPort, cByteToSend, comNO_BLOCK ) == pdPASS )
			  {
				//vParTestToggleLED( uxBaseLED + comTX_LED_OFFSET );
                PORTD=0xF0;
			  }
		    }
            xSerialPutChar( xPort, '\n', comNO_BLOCK);
		    xSerialPutChar( xPort, '\r', comNO_BLOCK);
            //PORTD=0xF0;
            vTaskDelay(100);
			xSemaphoreGive(xSem);
		} 
		else {
		} 
		vTaskDelay(100);
		i++;
	}
}

void Task2(void *params) {
signed char cByteToSend;
	taskENTER_CRITICAL();
	while( xSem == NULL )
		vTaskDelay(1);
	taskEXIT_CRITICAL();

	while(1) {				
		if(xSemaphoreTake(xSem, (portTickType) 10) == pdTRUE) {
			//puts("1234");
            //putrs1USART("1234\n\r");
            for( cByteToSend = 'G'; cByteToSend <= 'L'; cByteToSend++ )
		    {
			  if( xSerialPutChar( xPort, cByteToSend, comNO_BLOCK ) == pdPASS )
			  {
				//vParTestToggleLED( uxBaseLED + comTX_LED_OFFSET );
                PORTD=0x0F;
			  }
		    }
            xSerialPutChar( xPort, '\n', comNO_BLOCK);
		    xSerialPutChar( xPort, '\r', comNO_BLOCK);
            //PORTD=0x0F;
            vTaskDelay(100);
			xSemaphoreGive(xSem);
		} 
		else {
		}
		vTaskDelay(100);
		j++;
	}
}


void Task3(void *params) {
signed char cByteToSend;
signed char cByteRxed;

	while(1) {				
	      /* Block on the queue that contains received bytes until a byte is
			available. */
			if( xSerialGetChar( xPort, &cByteRxed, mainRX_BLOCK_TIME ) )
			{
              cByteToSend=cByteRxed;
			  if( xSerialPutChar( xPort, cByteToSend, comNO_BLOCK ) == pdPASS )
			  {
				//vParTestToggleLED( uxBaseLED + comTX_LED_OFFSET );
				PORTD=0x0F;
			  }
		    }
            //xSerialPutChar( xPort, '\n', comNO_BLOCK);
		    //xSerialPutChar( xPort, '\r', comNO_BLOCK);
 }  
}


//void vSerialTxISR()	{
//}

//void vSerialRxISR() {
//}

void main(void) {
	heapinit();

    TRISD = 0;              /* make Port D outputs */
    ANSELD = 0;             /* make it digital I/O */
    PORTD = 0x55;           /* show some pattern on LEDS */
	//OSCCON = 0b01110000; 	//8 MHz
	//OSCTUNE = 0b01011111;	//enable PLL
	//TRISC = 0x00;
	//stdout = _H_USART;
	//Open1USART(USART_TX_INT_OFF & USART_RX_INT_OFF & USART_ASYNCH_MODE & USART_EIGHT_BIT & USART_CONT_RX & USART_BRGH_LOW, 15);
	
    /* Send a character so we have some visible feedback of a reset. */
	xSerialPortInitMinimal( mainBAUD_RATE, mainCOMMS_QUEUE_LENGTH );
	xSerialPutChar( NULL, 'X', mainNO_BLOCK );


	xTaskCreate(Task1, (const portCHAR * const) "Ts1", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, NULL);
	xTaskCreate(Task2, (const portCHAR * const) "Ts2", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 2, NULL);
	xTaskCreate(Task3, (const portCHAR * const) "Ts3", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 3, NULL);
	vTaskStartScheduler();

	while(1) {
		ClrWdt();
	}
}
