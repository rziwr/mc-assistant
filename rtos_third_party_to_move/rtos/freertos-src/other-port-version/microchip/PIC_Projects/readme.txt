Create a new project here:

1) Open MPLAB
2) Project –> New…
   *) Project Name: RTOS_3
   *) Project Directory: C:\projects\microchip\PIC_Projects\RTOS_3
   *) OK
   *) The directory "C:\projects\microchip\PIC_Projects\RTOS_3" does not exist. Would you like to create it?
   *) OK
3) Configure –> Select Device…
   *) PIC18LF45K22
   *) OK
4) Project –> Build Options –> Project…
   *) Directories tab
      **) Show directories for: Library Search Path
      
      ***) New
      ***) C:\Program Files\Microchip\mplabc18\v3.39\lib
      
      **) Show directories for: Include Search Path
      ***) New
      ****) .
      ***) New 
      ****) ..\FreeRTOS\Source\Portable\PIC18
      ***) New
      ****) ..\FreeRTOS\Source\include
      ***) OK
5) In the MPASM/C17/C18 Suite tab
   *) Enable the checkbox for Extended mode
6) In the MPLAB C18 tab
   *) Categories: General
   **) Preprocessor Macros 
   ***) Add
   ***) MPLAB_PIC18F_PORT
   ***) Add
   ***) PV_PORT_MALLOC_ALIGNED_FIX
   *) Categories: Memory Model
   **) Large code model
   **) Large data model
   **) Multi-bank model
   *) Apply
   *) OK
7) View->Project
   *) Source Files
   **) Everything in the FreeRTOS\Source (croutine.c, list.c, queue.c, tasks.c, timers.c)
   **) Everything in the FreeRTOS\Source\portable\PIC18 directory 
   *) Header Files
   **) FreeRTOSConfig.h (copy over from RTOS_2 as a starting point)
   *) Linker Script
   **) portable/PIC18/18lf45k22_g_FreeRTOS.lkr

   *) More source files
   **) main.c (copy over from RTOS_2 as a starting point)   

   *) Project->Save Project
   *) File->Save Workspace as 
   **) RTOS_3.mcw

8) Build/run to see if you got the settings right and that it actually works
