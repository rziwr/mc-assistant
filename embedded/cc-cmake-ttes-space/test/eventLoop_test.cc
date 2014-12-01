#include "canary/config.h"

// Third party
#include <gtest/gtest.h>

// App
#ifdef __cplusplus
extern "C" {
#endif

#include "canary/vm/vm.h"
#include "canary/engine/eventLoop.h"
#include "canary/engine/onChain.h"

#ifdef __cplusplus
}
#endif

// --gtest_filter=Blocked*
TEST(BlockedLoop, Create) {
  vmInitialize_void();

  // Just example
  onSignal();

  // Launch event loop
  eloopIteration_void();
}
