# WAITRETRACE

## Syntax

```
WaitRetrace(nrOfFrames)
```

## Description

Waits for rasterline 0 for a number of loops (nrOfTimes), ignores keypresses.

**Example**

To use instead of **PAUSE 1**

	DO
		PRINT a
		a = a + 1
		WaitRetrace(1)
	LOOP

**Remarks**

Requires: 

	#INCLUDE <nextlib.bas>

Use instead of PAUSE 1
