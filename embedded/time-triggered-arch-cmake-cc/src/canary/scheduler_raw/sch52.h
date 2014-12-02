#ifndef RAW_SCH51_H_
#define RAW_SCH51_H_

#include "canary/scheduler_raw/main.h"

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

// FIXME: как быть с прочими прерываниями? ADC and UART

void SCH_Init_T2(void);
void SCH_Start(void);
void SCH_Dispatch_Tasks(void);

#endif  // RAW_SCH51_H_
