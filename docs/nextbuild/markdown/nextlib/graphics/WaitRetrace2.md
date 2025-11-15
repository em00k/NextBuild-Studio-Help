# WAITRETRACE2

## Syntax

```
WaitRetrace2(nrOfFrames)
```

## Description

This command is deprecated, use [WaitRaster()](WaitRaster.md) instead.
Classic Nextlib rasterline wait (nrOfFrames), ignores keypresses, doesn't disable interrupts.

**Example**

To use instead of **PAUSE 1**

	DO
		PRINT a
		a = a + 1
		WaitRetrace2(1)
	LOOP

**Remarks**

Requires: 

	#INCLUDE <nextlib.bas>

You can now use WaitRaster() which is easier to read. 
