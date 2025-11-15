# WaitRaster

## Syntax

```
WaitRaster(raster line)
```

## Description

Waits for "raster line" before continuing. Use this for timing. 

**Example**
```
' Wait for raster line 192
DO
	BORDER 2
	WaitRaster(192)
	BORDER 0
LOOP
```
**Remarks**

Requires: 

	#INCLUDE <nextlib.bas>

Use instead of PAUSE 0
