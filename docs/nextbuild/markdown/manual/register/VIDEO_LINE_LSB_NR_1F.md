# VIDEO_LINE_LSB_NR_1F

## Syntax

```
VIDEO_LINE_LSB_NR_1F = $1F
```

## Description

**ACTIVE VIDEO LINE LSB REGISTER**

More info : https://wiki.specnext.dev/Active_Video_Line_LSB_Register

Holds the eight LSBs of the raster line currently being drawn.(R)

The MSB of the raster line is in Active Video Line MSB Register ($1E).

The line coordinates use coordinate system of Copper coprocessor, i.e. line 0 is the first line of pixels.

Since core 3.1.5 the numbering of lines can be offset by Vertical Video Line Offset Register ($64).

Requires: 

	#INCLUDE <nextlib.bas>
