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

// FIXME: pic18 - may be troubles with fptrs
// "c18 c compiler user’s guide"
// http://www.electro-tech-online.com/threads/problem-in-using-pointer-functions-in-c18-compiler.88502/
// http://stackoverflow.com/questions/18211337/24-bit-const-pointers-on-xc8-pic18-not-workings
//
// But:
//  http://www.microchip.com/forums/m116960.aspx
//
// Compilators:
//   http://stackoverflow.com/questions/93356/what-is-the-best-c-complier-for-the-pic18-micro

// Conclusion:
//   Many troubles with config, but then easer
//   Продакшен версия будет не такой как тестовая. Задачи можно те же, а сам планировщик будет
//   другим.

#endif  // RAW_SCH51_H_
