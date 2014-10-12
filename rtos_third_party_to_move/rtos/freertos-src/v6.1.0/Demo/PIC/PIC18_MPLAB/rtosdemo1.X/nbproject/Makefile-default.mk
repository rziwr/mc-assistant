#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Include project Makefile
include Makefile
# Include makefile containing local settings
ifeq "$(wildcard nbproject/Makefile-local-default.mk)" "nbproject/Makefile-local-default.mk"
include nbproject/Makefile-local-default.mk
endif

# Environment
MKDIR=gnumkdir -p
RM=rm -f 
MV=mv 
CP=cp 

# Macros
CND_CONF=default
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
IMAGE_TYPE=debug
OUTPUT_SUFFIX=cof
DEBUGGABLE_SUFFIX=cof
FINAL_IMAGE=dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
else
IMAGE_TYPE=production
OUTPUT_SUFFIX=hex
DEBUGGABLE_SUFFIX=cof
FINAL_IMAGE=dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
endif

# Object Directory
OBJECTDIR=build/${CND_CONF}/${IMAGE_TYPE}

# Distribution Directory
DISTDIR=dist/${CND_CONF}/${IMAGE_TYPE}

# Object Files Quoted if spaced
OBJECTFILES_QUOTED_IF_SPACED=${OBJECTDIR}/_ext/449926602/tasks.o ${OBJECTDIR}/_ext/449926602/queue.o ${OBJECTDIR}/_ext/449926602/list.o ${OBJECTDIR}/_ext/820566071/port.o ${OBJECTDIR}/_ext/1163846883/PollQ.o ${OBJECTDIR}/_ext/1472/main1.o ${OBJECTDIR}/_ext/809743516/ParTest.o ${OBJECTDIR}/_ext/821501661/serial.o ${OBJECTDIR}/_ext/1163846883/integer.o ${OBJECTDIR}/_ext/1884096877/heap_1.o
POSSIBLE_DEPFILES=${OBJECTDIR}/_ext/449926602/tasks.o.d ${OBJECTDIR}/_ext/449926602/queue.o.d ${OBJECTDIR}/_ext/449926602/list.o.d ${OBJECTDIR}/_ext/820566071/port.o.d ${OBJECTDIR}/_ext/1163846883/PollQ.o.d ${OBJECTDIR}/_ext/1472/main1.o.d ${OBJECTDIR}/_ext/809743516/ParTest.o.d ${OBJECTDIR}/_ext/821501661/serial.o.d ${OBJECTDIR}/_ext/1163846883/integer.o.d ${OBJECTDIR}/_ext/1884096877/heap_1.o.d

# Object Files
OBJECTFILES=${OBJECTDIR}/_ext/449926602/tasks.o ${OBJECTDIR}/_ext/449926602/queue.o ${OBJECTDIR}/_ext/449926602/list.o ${OBJECTDIR}/_ext/820566071/port.o ${OBJECTDIR}/_ext/1163846883/PollQ.o ${OBJECTDIR}/_ext/1472/main1.o ${OBJECTDIR}/_ext/809743516/ParTest.o ${OBJECTDIR}/_ext/821501661/serial.o ${OBJECTDIR}/_ext/1163846883/integer.o ${OBJECTDIR}/_ext/1884096877/heap_1.o


CFLAGS=
ASFLAGS=
LDLIBSOPTIONS=

############# Tool locations ##########################################
# If you copy a project from one host to another, the path where the  #
# compiler is installed may be different.                             #
# If you open this project with MPLAB X in the new host, this         #
# makefile will be regenerated and the paths will be corrected.       #
#######################################################################
# fixDeps replaces a bunch of sed/cat/printf statements that slow down the build
FIXDEPS=fixDeps

.build-conf:  ${BUILD_SUBPROJECTS}
	${MAKE} ${MAKE_OPTIONS} -f nbproject/Makefile-default.mk dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}

MP_PROCESSOR_OPTION=18F8722
MP_PROCESSOR_OPTION_LD=18f8722
MP_LINKER_DEBUG_OPTION= -u_DEBUGCODESTART=0x1fd30 -u_DEBUGCODELEN=0x2d0 -u_DEBUGDATASTART=0xef4 -u_DEBUGDATALEN=0xb
# ------------------------------------------------------------------------------------
# Rules for buildStep: assemble
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: compile
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
${OBJECTDIR}/_ext/449926602/tasks.o: ../../../Source/tasks.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/449926602 
	@${RM} ${OBJECTDIR}/_ext/449926602/tasks.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/449926602/tasks.o   ../../../Source/tasks.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/449926602/tasks.o 
	
${OBJECTDIR}/_ext/449926602/queue.o: ../../../Source/queue.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/449926602 
	@${RM} ${OBJECTDIR}/_ext/449926602/queue.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/449926602/queue.o   ../../../Source/queue.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/449926602/queue.o 
	
${OBJECTDIR}/_ext/449926602/list.o: ../../../Source/list.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/449926602 
	@${RM} ${OBJECTDIR}/_ext/449926602/list.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/449926602/list.o   ../../../Source/list.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/449926602/list.o 
	
${OBJECTDIR}/_ext/820566071/port.o: ../../../Source/portable/MPLAB/PIC18F/port.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/820566071 
	@${RM} ${OBJECTDIR}/_ext/820566071/port.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/820566071/port.o   ../../../Source/portable/MPLAB/PIC18F/port.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/820566071/port.o 
	
${OBJECTDIR}/_ext/1163846883/PollQ.o: ../../Common/Minimal/PollQ.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1163846883 
	@${RM} ${OBJECTDIR}/_ext/1163846883/PollQ.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1163846883/PollQ.o   ../../Common/Minimal/PollQ.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1163846883/PollQ.o 
	
${OBJECTDIR}/_ext/1472/main1.o: ../main1.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1472 
	@${RM} ${OBJECTDIR}/_ext/1472/main1.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1472/main1.o   ../main1.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1472/main1.o 
	
${OBJECTDIR}/_ext/809743516/ParTest.o: ../ParTest/ParTest.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/809743516 
	@${RM} ${OBJECTDIR}/_ext/809743516/ParTest.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/809743516/ParTest.o   ../ParTest/ParTest.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/809743516/ParTest.o 
	
${OBJECTDIR}/_ext/821501661/serial.o: ../serial/serial.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/821501661 
	@${RM} ${OBJECTDIR}/_ext/821501661/serial.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/821501661/serial.o   ../serial/serial.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/821501661/serial.o 
	
${OBJECTDIR}/_ext/1163846883/integer.o: ../../Common/Minimal/integer.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1163846883 
	@${RM} ${OBJECTDIR}/_ext/1163846883/integer.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1163846883/integer.o   ../../Common/Minimal/integer.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1163846883/integer.o 
	
${OBJECTDIR}/_ext/1884096877/heap_1.o: ../../../Source/portable/MemMang/heap_1.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1884096877 
	@${RM} ${OBJECTDIR}/_ext/1884096877/heap_1.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1884096877/heap_1.o   ../../../Source/portable/MemMang/heap_1.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1884096877/heap_1.o 
	
else
${OBJECTDIR}/_ext/449926602/tasks.o: ../../../Source/tasks.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/449926602 
	@${RM} ${OBJECTDIR}/_ext/449926602/tasks.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/449926602/tasks.o   ../../../Source/tasks.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/449926602/tasks.o 
	
${OBJECTDIR}/_ext/449926602/queue.o: ../../../Source/queue.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/449926602 
	@${RM} ${OBJECTDIR}/_ext/449926602/queue.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/449926602/queue.o   ../../../Source/queue.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/449926602/queue.o 
	
${OBJECTDIR}/_ext/449926602/list.o: ../../../Source/list.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/449926602 
	@${RM} ${OBJECTDIR}/_ext/449926602/list.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/449926602/list.o   ../../../Source/list.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/449926602/list.o 
	
${OBJECTDIR}/_ext/820566071/port.o: ../../../Source/portable/MPLAB/PIC18F/port.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/820566071 
	@${RM} ${OBJECTDIR}/_ext/820566071/port.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/820566071/port.o   ../../../Source/portable/MPLAB/PIC18F/port.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/820566071/port.o 
	
${OBJECTDIR}/_ext/1163846883/PollQ.o: ../../Common/Minimal/PollQ.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1163846883 
	@${RM} ${OBJECTDIR}/_ext/1163846883/PollQ.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1163846883/PollQ.o   ../../Common/Minimal/PollQ.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1163846883/PollQ.o 
	
${OBJECTDIR}/_ext/1472/main1.o: ../main1.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1472 
	@${RM} ${OBJECTDIR}/_ext/1472/main1.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1472/main1.o   ../main1.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1472/main1.o 
	
${OBJECTDIR}/_ext/809743516/ParTest.o: ../ParTest/ParTest.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/809743516 
	@${RM} ${OBJECTDIR}/_ext/809743516/ParTest.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/809743516/ParTest.o   ../ParTest/ParTest.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/809743516/ParTest.o 
	
${OBJECTDIR}/_ext/821501661/serial.o: ../serial/serial.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/821501661 
	@${RM} ${OBJECTDIR}/_ext/821501661/serial.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/821501661/serial.o   ../serial/serial.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/821501661/serial.o 
	
${OBJECTDIR}/_ext/1163846883/integer.o: ../../Common/Minimal/integer.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1163846883 
	@${RM} ${OBJECTDIR}/_ext/1163846883/integer.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1163846883/integer.o   ../../Common/Minimal/integer.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1163846883/integer.o 
	
${OBJECTDIR}/_ext/1884096877/heap_1.o: ../../../Source/portable/MemMang/heap_1.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/1884096877 
	@${RM} ${OBJECTDIR}/_ext/1884096877/heap_1.o.d 
	${MP_CC} $(MP_EXTRA_CC_PRE) -p$(MP_PROCESSOR_OPTION) -w3 -DMPLAB_PIC18F_PORT -I".." -I"../include" -I"../../include" -I"../../../include" -I"../../../../include" -I"../../../Source/include" -I"../../../../Source/include" -I"../../Demo/PIC18_MPLAB" -I"../../../../Demo/PIC18_MPLAB" -I"../../../../../Demo/PIC18_MPLAB" -I"C:/Devtools/Microchip/MCC18/h" -I"../../Common/include" -I"../../../Common/include" -I"../../../Source/portable/MPLAB/PIC18F" -Ls -Opa- -nw 2074 -nw 2066  -I ${MP_CC_DIR}\\..\\h  -fo ${OBJECTDIR}/_ext/1884096877/heap_1.o   ../../../Source/portable/MemMang/heap_1.c  -nw 2074 -nw 2066
	@${DEP_GEN} -d ${OBJECTDIR}/_ext/1884096877/heap_1.o 
	
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: link
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk   
	@${MKDIR} dist/${CND_CONF}/${IMAGE_TYPE} 
	${MP_LD} $(MP_EXTRA_LD_PRE) "..\18f452.lkr"  -p$(MP_PROCESSOR_OPTION_LD)  -w -x -u_DEBUG -m"$(BINDIR_)$(TARGETBASE).map" -aINHX8M -l"C:/Devtools/Microchip/MCC18/lib" /p 18F452  -z__MPLAB_BUILD=1  -u_CRUNTIME -z__MPLAB_DEBUG=1 -z__MPLAB_DEBUGGER_ICD3=1 $(MP_LINKER_DEBUG_OPTION) -l ${MP_CC_DIR}\\..\\lib  -o dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}  ${OBJECTFILES_QUOTED_IF_SPACED}    /p 18F452
else
dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk   
	@${MKDIR} dist/${CND_CONF}/${IMAGE_TYPE} 
	${MP_LD} $(MP_EXTRA_LD_PRE) "..\18f452.lkr"  -p$(MP_PROCESSOR_OPTION_LD)  -w  -m"$(BINDIR_)$(TARGETBASE).map" -aINHX8M -l"C:/Devtools/Microchip/MCC18/lib" /p 18F452  -z__MPLAB_BUILD=1  -u_CRUNTIME -l ${MP_CC_DIR}\\..\\lib  -o dist/${CND_CONF}/${IMAGE_TYPE}/rtosdemo1.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX}  ${OBJECTFILES_QUOTED_IF_SPACED}    /p 18F452
endif


# Subprojects
.build-subprojects:


# Subprojects
.clean-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r build/default
	${RM} -r dist/default

# Enable dependency checking
.dep.inc: .depcheck-impl

DEPFILES=$(shell mplabwildcard ${POSSIBLE_DEPFILES})
ifneq (${DEPFILES},)
include ${DEPFILES}
endif
