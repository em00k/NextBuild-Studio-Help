# DEFINE

## Syntax

```
#DEFINE *def*
```

## Description

Sets a compiler DEFINE. nextlibs.bas make use of DEFINES in the following way.

	#DEFINE IM2 : REM Using the AYFX & Music player routines
	#DEFINE NEX : REM Producing a final NEX (disables LoadSDBank code)
	#DEFINE DEBUG : REM Displays warnings when loadsd fails

**Examples**

Output a final NEX

	#DEFINE NEX
	#INCLUDE \<nextlib.bas\>

You are using your own interrupt & final NEX

	#DEFINE IM2
	#DEFINE NEX
	#INCLUDE <nextlib.bas>

**NB** The DEFINE needs to be set before 	#INCLUDE \<nextlib.bas\>
