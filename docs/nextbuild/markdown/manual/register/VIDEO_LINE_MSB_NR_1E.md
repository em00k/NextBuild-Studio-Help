# VIDEO_LINE_MSB_NR_1E

## Syntax

```
VIDEO_LINE_MSB_NR_1E = $1E
```

## Description

**ACTIVE VIDEO LINE MSB REGISTER**

More info : https://wiki.specnext.dev/Active_Video_Line_MSB_Register

Holds the MSB (only, as bit 0) of the raster line currently being drawn.(R)

The low 8 bit part of the raster line number is in Active Video Line LSB Register ($1F).

The line coordinates use coordinate system of Copper coprocessor, i.e. line 0 is the first line of pixels.

Since core 3.1.5 the numbering of lines can be offset by Vertical Video Line Offset Register ($64).

Requires: 

	#INCLUDE <nextlib.bas>
