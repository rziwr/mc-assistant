# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.1

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files (x86)\CMake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files (x86)\CMake\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\work\apps\mc-assistant\embedded\cc-cmake-test

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\work\apps\mc-assistant\embedded\cc-cmake-test-build

# Include any dependencies generated for this target.
include CMakeFiles/cc-cmake-test.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cc-cmake-test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cc-cmake-test.dir/flags.make

CMakeFiles/cc-cmake-test.dir/main.cpp.obj: CMakeFiles/cc-cmake-test.dir/flags.make
CMakeFiles/cc-cmake-test.dir/main.cpp.obj: D:/work/apps/mc-assistant/embedded/cc-cmake-test/main.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report D:\work\apps\mc-assistant\embedded\cc-cmake-test-build\CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/cc-cmake-test.dir/main.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.2-W\mingw64\bin\G__~1.EXE   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles\cc-cmake-test.dir\main.cpp.obj -c D:\work\apps\mc-assistant\embedded\cc-cmake-test\main.cpp

CMakeFiles/cc-cmake-test.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cc-cmake-test.dir/main.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.2-W\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_FLAGS) -E D:\work\apps\mc-assistant\embedded\cc-cmake-test\main.cpp > CMakeFiles\cc-cmake-test.dir\main.cpp.i

CMakeFiles/cc-cmake-test.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cc-cmake-test.dir/main.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.2-W\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_FLAGS) -S D:\work\apps\mc-assistant\embedded\cc-cmake-test\main.cpp -o CMakeFiles\cc-cmake-test.dir\main.cpp.s

CMakeFiles/cc-cmake-test.dir/main.cpp.obj.requires:
.PHONY : CMakeFiles/cc-cmake-test.dir/main.cpp.obj.requires

CMakeFiles/cc-cmake-test.dir/main.cpp.obj.provides: CMakeFiles/cc-cmake-test.dir/main.cpp.obj.requires
	$(MAKE) -f CMakeFiles\cc-cmake-test.dir\build.make CMakeFiles/cc-cmake-test.dir/main.cpp.obj.provides.build
.PHONY : CMakeFiles/cc-cmake-test.dir/main.cpp.obj.provides

CMakeFiles/cc-cmake-test.dir/main.cpp.obj.provides.build: CMakeFiles/cc-cmake-test.dir/main.cpp.obj

# Object files for target cc-cmake-test
cc__cmake__test_OBJECTS = \
"CMakeFiles/cc-cmake-test.dir/main.cpp.obj"

# External object files for target cc-cmake-test
cc__cmake__test_EXTERNAL_OBJECTS =

cc-cmake-test.exe: CMakeFiles/cc-cmake-test.dir/main.cpp.obj
cc-cmake-test.exe: CMakeFiles/cc-cmake-test.dir/build.make
cc-cmake-test.exe: CMakeFiles/cc-cmake-test.dir/linklibs.rsp
cc-cmake-test.exe: CMakeFiles/cc-cmake-test.dir/objects1.rsp
cc-cmake-test.exe: CMakeFiles/cc-cmake-test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable cc-cmake-test.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\cc-cmake-test.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cc-cmake-test.dir/build: cc-cmake-test.exe
.PHONY : CMakeFiles/cc-cmake-test.dir/build

CMakeFiles/cc-cmake-test.dir/requires: CMakeFiles/cc-cmake-test.dir/main.cpp.obj.requires
.PHONY : CMakeFiles/cc-cmake-test.dir/requires

CMakeFiles/cc-cmake-test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\cc-cmake-test.dir\cmake_clean.cmake
.PHONY : CMakeFiles/cc-cmake-test.dir/clean

CMakeFiles/cc-cmake-test.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\work\apps\mc-assistant\embedded\cc-cmake-test D:\work\apps\mc-assistant\embedded\cc-cmake-test D:\work\apps\mc-assistant\embedded\cc-cmake-test-build D:\work\apps\mc-assistant\embedded\cc-cmake-test-build D:\work\apps\mc-assistant\embedded\cc-cmake-test-build\CMakeFiles\cc-cmake-test.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/cc-cmake-test.dir/depend

