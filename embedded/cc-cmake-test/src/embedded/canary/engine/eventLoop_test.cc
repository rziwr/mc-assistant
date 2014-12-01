#include "embedded/canary/config.h"

// Third party
#include <gtest/gtest.h>

// App
#include "embedded/canary/engine/vm.h"
#include "embedded/canary/engine/eventLoop.h"
#include "embedded/canary/signals_slots/onChain.h"

// --gtest_filter=Blocked*
TEST(BlockedLoop, Create) {
  vmInitialize_void();

  // Just example
  onSignal();

  // Launch event loop
  evlRun_void();
}
