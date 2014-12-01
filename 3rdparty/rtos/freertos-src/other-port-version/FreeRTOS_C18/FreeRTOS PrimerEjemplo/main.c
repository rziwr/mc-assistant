#include <p18f4620.h>

/** CONFIGURATION **************************************************/
#pragma config OSC=HSPLL
#pragma config IESO=OFF
#pragma config PWRT=ON
#pragma config WDT=OFF
#pragma config MCLRE=ON
#pragma config XINST=OFF
#pragma config DEBUG=OFF
#pragma config FCMEN = OFF
#pragma config LVP=OFF
#pragma config BOREN=OFF
#pragma config PBADEN = OFF
/** END CONFIGURATION **************************************************/
#include "FreeRTOS.h"
#include "task.h"

#define PRIORITY_TASK0		( tskIDLE_PRIORITY + 1 )
#define PRIORITY_TASK1		( tskIDLE_PRIORITY + 1 )
/*************************** Tasks Prototypes ****************************/
static void vTASK0( void *pvParameters );
static void vTASK1( void *pvParameters );
/*-----------------------------------------------------------*/
void main( void ){
	TRISB=0x00;
	vPortInitialiseBlocks();

	xTaskCreate( vTASK0, ( const char * const ) "T0", configMINIMAL_STACK_SIZE, NULL, PRIORITY_TASK0, NULL );
	xTaskCreate( vTASK1, ( const char * const ) "T1", configMINIMAL_STACK_SIZE, NULL, PRIORITY_TASK1, NULL );

	vTaskStartScheduler();
}
/*-----------------------------------------------------------*/
static void vTASK0( void *pvParameters ){
	while(1)
	{
		LATBbits.LATB0=!PORTBbits.RB0;
		vTaskDelay(250/portTICK_RATE_MS);
	}
}
/*-----------------------------------------------------------*/
static void vTASK1( void *pvParameters ){
	while(1){
		LATBbits.LATB1=!PORTBbits.RB1;
		vTaskDelay(350/portTICK_RATE_MS);
	}
}