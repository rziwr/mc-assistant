#include "canary/config.h"  // in every *.c or *.cc file
#include "canary/engine/eventLoop.h"

// App
#include "canary/engine/onChain.h"

//static
void eloopIteration_void() {
  onSlot();
  //lockSlot();
  //ulockSlot();
  //offSlot();
  //otherSlot();
}

void eloopRunSuperLoop_void() {
  while(1) {
    eloopIteration_void();
    break;  // TODO: remove it
  }
}

void eloopStop_void() {
  // TODO: some action
}
