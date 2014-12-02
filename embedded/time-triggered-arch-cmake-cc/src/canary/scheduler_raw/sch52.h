#ifndef RAW_SCH51_H_
#define RAW_SCH51_H_

#include "canary/scheduler_raw/main.h"

// Store in DATA area, if possible, for rapid access
// Total memory per task is 7 bytes
typedef /*data*/ struct
{
  // Pointer to the task (must be a 'void (void)' function)

  void (/*code*/ * pTask)(void);  // FIXME: unknown option

  // Delay (ticks) until the function will (next) be run
  // - see SCH_Add_Task() for further details
  tWord Delay;
  // Interval (ticks) between subsequent runs.
  // - see SCH_Add_Task() for further details
  tWord Period;
  // Incremented (by scheduler) when task is due to execute
  tByte RunMe;
} sTask;

#endif  // RAW_SCH51_H_
