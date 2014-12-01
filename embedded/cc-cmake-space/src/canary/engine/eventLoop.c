#include "canary/config.h"  // in every *.c or *.cc file
#include "canary/engine/eventLoop.h"

// App
#include "canary/engine/onChain.h"

void evlRun_void() {
  while(1) {
    onSlot();
    //lockSlot();
    //ulockSlot();
    //offSlot();
    //otherSlot();
    break;  // TODO: remove it
  }
}

void evlStop_void() {
  // TODO: some action
}
