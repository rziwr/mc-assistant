#include "embedded/canary/config.h"  // in every *.c or *.cc file


// App
#include "embedded/canary/virtual_devices/virtualDvrPreampl.h"

int onCounter = 0;
static const int kOnCounter = 10;

void onSignal() {
  // TODO:
  /// begin atomic

  /// end atomic
}

void onSlot() {
  // TODO: Some action
  /// begin atomic

  /// end atomic

  // !! Work if tack is active
  preamplReset_void_Virtual();
}
