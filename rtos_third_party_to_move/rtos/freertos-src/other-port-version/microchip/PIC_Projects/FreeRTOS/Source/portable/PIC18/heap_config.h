#if	0
//==============================================================================
// This file is part of "Heap Management For Small Microcontrollers".
// v1.04 (2009-05-23)
// isaacbavaresco@yahoo.com.br
//==============================================================================
/*
 Copyright (c) 2007-2009, Isaac Marino Bavaresco
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:
     * Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
     * Neither the name of the author nor the
       names of its contributors may be used to endorse or promote products
       derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY
 EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
 DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
//==============================================================================
//
// This file is included from both ".c" files and ".asm" files.
//
//==============================================================================
#endif

#define USING_FREE_RTOS			0

#if 0
//   If your stack is located after and contiguous to the heap, you can
//   define the macro "ALLOCATE_FROM_BEGINNING" to "1" so both get merged
//   together and the free space is in one single piece.
//
//   If the stack is located before and contiguous to the heap, the it is
//   better to leave "ALLOCATE_FROM_BEGINNING" as "0".
//
//   If you don't do so, your free space in the final heap will be split in
//   two non contiguous areas.
//
//   Using "ALLOCATE_FROM_BEGINNING" with a value of zero is marginally more
//   efficient.
#endif

#define ALLOCATE_FROM_BEGINNING	1

#define	HEAP_SIZE				1024

#if 0
// Be careful, this definition should agree with the linker-script
// or it must be zero.
// If STACK_SIZE is defined to zero, __reclaim_stack() is not defined.
#endif
#define STACK_SIZE				0x100

