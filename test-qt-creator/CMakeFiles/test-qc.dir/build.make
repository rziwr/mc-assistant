# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files (x86)\CMake 2.8\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = "C:\Program Files (x86)\CMake 2.8\bin\cmake-gui.exe"

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\github-develop\mc-assistant\test-qt-creator\test-qc

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\github-develop\mc-assistant\test-qt-creator

# Include any dependencies generated for this target.
include CMakeFiles\test-qc.dir\depend.make

# Include the progress variables for this target.
include CMakeFiles\test-qc.dir\progress.make

# Include the compile flags for this target's objects.
include CMakeFiles\test-qc.dir\flags.make

CMakeFiles\test-qc.dir\main.c.obj: CMakeFiles\test-qc.dir\flags.make
CMakeFiles\test-qc.dir\main.c.obj: test-qc\main.c
	$(CMAKE_COMMAND) -E cmake_progress_report D:\github-develop\mc-assistant\test-qt-creator\CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/test-qc.dir/main.c.obj"
	C:\PROGRA~2\MICROS~1.0\VC\bin\cl.exe  @<<
 /nologo $(C_FLAGS) $(C_DEFINES) /FoCMakeFiles\test-qc.dir\main.c.obj /FdD:\github-develop\mc-assistant\test-qt-creator\test-qc.pdb -c D:\github-develop\mc-assistant\test-qt-creator\test-qc\main.c
<<

CMakeFiles\test-qc.dir\main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test-qc.dir/main.c.i"
	C:\PROGRA~2\MICROS~1.0\VC\bin\cl.exe  > CMakeFiles\test-qc.dir\main.c.i @<<
 /nologo $(C_FLAGS) $(C_DEFINES) -E D:\github-develop\mc-assistant\test-qt-creator\test-qc\main.c
<<

CMakeFiles\test-qc.dir\main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test-qc.dir/main.c.s"
	C:\PROGRA~2\MICROS~1.0\VC\bin\cl.exe  @<<
 /nologo $(C_FLAGS) $(C_DEFINES) /FoNUL /FAs /FaCMakeFiles\test-qc.dir\main.c.s /c D:\github-develop\mc-assistant\test-qt-creator\test-qc\main.c
<<

CMakeFiles\test-qc.dir\main.c.obj.requires:
.PHONY : CMakeFiles\test-qc.dir\main.c.obj.requires

CMakeFiles\test-qc.dir\main.c.obj.provides: CMakeFiles\test-qc.dir\main.c.obj.requires
	$(MAKE) -f CMakeFiles\test-qc.dir\build.make /nologo -$(MAKEFLAGS) CMakeFiles\test-qc.dir\main.c.obj.provides.build
.PHONY : CMakeFiles\test-qc.dir\main.c.obj.provides

CMakeFiles\test-qc.dir\main.c.obj.provides.build: CMakeFiles\test-qc.dir\main.c.obj

# Object files for target test-qc
test__qc_OBJECTS = \
"CMakeFiles\test-qc.dir\main.c.obj"

# External object files for target test-qc
test__qc_EXTERNAL_OBJECTS =

test-qc.exe: CMakeFiles\test-qc.dir\main.c.obj
test-qc.exe: CMakeFiles\test-qc.dir\build.make
test-qc.exe: CMakeFiles\test-qc.dir\objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable test-qc.exe"
	"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E vs_link_exe C:\PROGRA~2\MICROS~1.0\VC\bin\cl.exe  /nologo @<<
  /DWIN32 /D_WINDOWS /W3 /Zm1000 /D_DEBUG /MDd /Zi /Ob0 /Od /RTC1 /Fetest-qc.exe /FdD:\github-develop\mc-assistant\test-qt-creator\test-qc.pdb @CMakeFiles\test-qc.dir\objects1.rsp /link /implib:test-qc.lib /version:0.0   /STACK:10000000 /machine:X86  /debug /INCREMENTAL:YES /subsystem:console  kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib 
<<

# Rule to build all files generated by this target.
CMakeFiles\test-qc.dir\build: test-qc.exe
.PHONY : CMakeFiles\test-qc.dir\build

CMakeFiles\test-qc.dir\requires: CMakeFiles\test-qc.dir\main.c.obj.requires
.PHONY : CMakeFiles\test-qc.dir\requires

CMakeFiles\test-qc.dir\clean:
	$(CMAKE_COMMAND) -P CMakeFiles\test-qc.dir\cmake_clean.cmake
.PHONY : CMakeFiles\test-qc.dir\clean

CMakeFiles\test-qc.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" D:\github-develop\mc-assistant\test-qt-creator\test-qc D:\github-develop\mc-assistant\test-qt-creator\test-qc D:\github-develop\mc-assistant\test-qt-creator D:\github-develop\mc-assistant\test-qt-creator D:\github-develop\mc-assistant\test-qt-creator\CMakeFiles\test-qc.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles\test-qc.dir\depend

