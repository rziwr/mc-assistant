#include "canary/scheduler_raw/main.h"
#include "canary/scheduler_raw/sch52.h"

static sTask SCH_tasks_G[SCH_MAX_TASKS];

static tByte Error_code_G;

/*------------------------------------------------------------------*/
//bit
tByte
SCH_Delete_Task(const tByte TASK_INDEX)
  {
  //bit
  tByte
  Return_code;
  if (SCH_tasks_G[TASK_INDEX].pTask == 0)
    {
    // No task at this location...
    //
    // Set the global error variable
    Error_code_G = ERROR_SCH_CANNOT_DELETE_TASK;

    // ...also return an error code
    Return_code = RETURN_ERROR;
    }
  else
    {
    Return_code = RETURN_NORMAL;
    }
  SCH_tasks_G[TASK_INDEX].pTask = 0x0000;
  SCH_tasks_G[TASK_INDEX].Delay = 0;
  SCH_tasks_G[TASK_INDEX].Period = 0;
  SCH_tasks_G[TASK_INDEX].RunMe = 0;
  return Return_code; // return status
  }

/*------------------------------------------------------------------*-
  SCH_Update()
  This is the scheduler ISR. It is called at a rate
  determined by the timer settings in the 'init' function.
  This version is triggered by Timer 2 interrupts:
  timer is automatically reloaded.
-*------------------------------------------------------------------*/
// FIXME: it's ISR?
void SCH_Update(void)  /*interrupt INTERRUPT_Timer_2_Overflow*/
  {
  tByte Index;
  /*TF2 = 0*/; // Have to manually clear this.
  // NOTE: calculations are in *TICKS* (not milliseconds)
  for (Index = 0; Index < SCH_MAX_TASKS; Index++) {
    // Check if there is a task at this location
    if (SCH_tasks_G[Index].pTask) {
      if (SCH_tasks_G[Index].Delay == 0) {
        // The task is due to run
        SCH_tasks_G[Index].RunMe += 1; // Inc. the 'RunMe' flag
        if (SCH_tasks_G[Index].Period)
          {
          // Schedule periodic tasks to run again
          SCH_tasks_G[Index].Delay = SCH_tasks_G[Index].Period;
          }
        }
      else {
          // Not yet ready to run: just decrement the delay
          SCH_tasks_G[Index].Delay -= 1;
          }
      }
    }
  }

/*------------------------------------------------------------------*-
  SCH_Add_Task()
  Causes a task (function) to be executed at regular intervals
  or after a user-defined delay
-*------------------------------------------------------------------*/
tByte SCH_Add_Task(
    void (/*code*/ * pFunction)(),
    const tWord DELAY,
    const tWord PERIOD)
  {
  tByte Index = 0;
  // First find a gap in the array (if there is one)
  while ((SCH_tasks_G[Index].pTask != 0) && (Index < SCH_MAX_TASKS))
    {
    Index++;
    }

  // Find identical task

  // Have we reached the end of the list?
  if (Index == SCH_MAX_TASKS)
    {
    // Task list is full
    //
    // Set the global error variable
    Error_code_G = ERROR_SCH_TOO_MANY_TASKS;
    // Also return an error code
    return SCH_MAX_TASKS;
    }

  // If we're here, there is a space in the task array
  SCH_tasks_G[Index].pTask = pFunction;
  SCH_tasks_G[Index].Delay = DELAY;
  SCH_tasks_G[Index].Period = PERIOD;
  SCH_tasks_G[Index].RunMe = 0;
  return Index; // return position of task (to allow later deletion)
}

/*------------------------------------------------------------------*-
SCH_Dispatch_Tasks()
This is the 'dispatcher' function. When a task (function)
is due to run, SCH_Dispatch_Tasks() will run it.
This function must be called (repeatedly) from the main loop.
-*------------------------------------------------------------------*/
void SCH_Dispatch_Tasks(void)
  {
  tByte Index;
  // Dispatches (runs) the next task (if one is ready)
  for (Index = 0; Index < SCH_MAX_TASKS; Index++)
    {
    if (SCH_tasks_G[Index].RunMe > 0)
      {
      (*SCH_tasks_G[Index].pTask)(); // Run the task
      SCH_tasks_G[Index].RunMe -= 1; // Reset / reduce RunMe flag
      // Periodic tasks will automatically run again
      // - if this is a 'one shot' task, remove it from the array
      if (SCH_tasks_G[Index].Period == 0)
        {
        SCH_Delete_Task(Index);
        }
      }
    }
  // Report system status
  //SCH_Report_Status();
  // The scheduler enters idle mode at this point

  // FIXME: не ясно как заменить
  //SCH_Go_To_Sleep();  // FIXME: very important
  }



