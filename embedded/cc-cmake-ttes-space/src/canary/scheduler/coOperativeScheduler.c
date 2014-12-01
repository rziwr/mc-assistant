#include "canary/config.h"  // in every *.c or *.cc file
#include "canary/scheduler/coOperativeScheduler.h"

// App
#include "canary/tasks/onChain.h"

//static
void coschIteration_void() {
  onSlot();
  //lockSlot();
  //ulockSlot();
  //offSlot();
  //otherSlot();
}

void coschRunLoop_void() {
  while(1) {
    coschIteration_void();
    break;  // TODO: remove it
  }
}

static
void coschStop_void() {
  // TODO: some action
}
