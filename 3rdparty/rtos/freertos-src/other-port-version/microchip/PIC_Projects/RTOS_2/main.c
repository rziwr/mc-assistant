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

#ifdef __18LF45K22
    #pragma config FCMEN = OFF
    #pragma config IESO = OFF
    #pragma config BOREN = OFF
    #pragma config LVP = OFF
    #pragma config XINST = ON
    #pragma config WDTEN = OFF
#endif

long int i, j = 0;
xSemaphoreHandle xSem = NULL;

void Task1(void *params) {
	__reclaim_stack();
	xSem = xSemaphoreCreateMutex();
	while(1) {		
		if(xSemaphoreTake(xSem, (portTickType) 10) == pdTRUE) {
			//puts("abcd");
            putrs1USART("abcd\n\r");
            PORTD=0xF0;
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
	taskENTER_CRITICAL();
	while( xSem == NULL )
		vTaskDelay(1);
	taskEXIT_CRITICAL();

	while(1) {				
		if(xSemaphoreTake(xSem, (portTickType) 10) == pdTRUE) {
			//puts("1234");
            putrs1USART("1234\n\r");
            PORTD=0x0F;
            vTaskDelay(100);
			xSemaphoreGive(xSem);
		} 
		else {
		}
		vTaskDelay(100);
		j++;
	}
}

void vSerialTxISR()	{
}

void vSerialRxISR() {
}

void main(void) {
	heapinit();

    TRISD = 0;              /* make Port D outputs */
    ANSELD = 0;             /* make it digital I/O */
    PORTD = 0x55;           /* show some pattern on LEDS */
	//OSCCON = 0b01110000; 	//8 MHz
	//OSCTUNE = 0b01011111;	//enable PLL
	//TRISC = 0x00;
	//stdout = _H_USART;
	Open1USART(USART_TX_INT_OFF & USART_RX_INT_OFF & USART_ASYNCH_MODE & USART_EIGHT_BIT & USART_CONT_RX & USART_BRGH_LOW, 15);
	
	xTaskCreate(Task1, (const portCHAR * const) "Ts1", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, NULL);
	xTaskCreate(Task2, (const portCHAR * const) "Ts2", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, NULL);
	vTaskStartScheduler();

	while(1) {
		ClrWdt();
	}
}
