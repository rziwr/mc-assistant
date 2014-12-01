#include "canary/config.h"

// Third party
#include <gtest/gtest.h>

// App
#include "canary/vm/vm.h"
#include "canary/engine/eventLoop.h"
#include "canary/engine/onChain.h"

// --gtest_filter=Blocked*
TEST(BlockedLoop, Create) {
  vmInitialize_void();

  // Just example
  onSignal();

  // Launch event loop
  evlRun_void();
}
