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

// Raw
#include "canary/scheduler_raw/sch52.h"

#ifdef __cplusplus
}
#endif

// --gtest_filter=Blocked*
TEST(BlockedLoop, Create) {
  vmInitialize_void();

  // Just example
  onSignal();

  // Launch event loop
  schDispatch_void();
}

TEST(SchPair, Base) {
  // FIXME: how replane on spot task

  // Add periodic tasks

  // Other tasks added from periodic tasks
  while(1) {
    //schDispatchPeriodic();

    // Self deleted tasks
    //schDispatchOneSpot();
    break;
  }
}
