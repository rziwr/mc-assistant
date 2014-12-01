#include "canary/config.h"

// Third party
#include <gtest/gtest.h>

// App
// So simpler
#ifdef __cplusplus
extern "C" {
#endif

#include "canary/vm/vm.h"
#include "canary/scheduler/coOperativeScheduler.h"
#include "canary/tasks/onChain.h"

#ifdef __cplusplus
}
#endif

// --gtest_filter=Blocked*
TEST(BlockedLoop, Create) {
  vmInitialize_void();

  // Just example
  onSignal();

  // Launch event loop
  coschIteration_void();
}
