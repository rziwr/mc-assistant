project(cc-cmake-test)
cmake_minimum_required(VERSION 2.8)

aux_source_directory(./src SRC_LIST)

set(GMock "../../3rdparty/gmock-1.6.0/fused-src")

# Test framework
include_directories(${GMock}/)

#file( GLOB  pureC  /src/*.cc)

add_executable(${PROJECT_NAME} ${SRC_LIST} "${GMock}/gmock-gtest-all.cc")

