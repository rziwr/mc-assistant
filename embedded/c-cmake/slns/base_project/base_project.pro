TEMPLATE = app
CONFIG += console
CONFIG -= qt

INCLUDEPATH += \
    ../../../third_party/gmock-1.6.0/fused-src \
    ../../src/

LIBS += -lpthread

SOURCES += \
    ../../src/launcher_tests.cc \
    ../../../third_party/gmock-1.6.0/fused-src/gmock-gtest-all.cc \
    ../../src/embedded/canary/engine/eventLoop_test.cc \
    ../../src/embedded/canary/engine/eventLoop.c \
    ../../src/embedded/canary/engine/vm.c \
    ../../src/embedded/canary/signals_slots/onChain.c \
    ../../src/embedded/canary/signals_slots/offChain.c \
    ../../src/embedded/canary/virtual_devices/virtualDvrPreampl.c \
    ../../src/embedded/canary/logical_devices/dvrOnBoardPreaml.c

HEADERS += \
    ../../src/embedded/canary/virtual_devices/virtualDvrPreampl.h

