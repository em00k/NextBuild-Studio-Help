# VIDEO_INTERUPT_VALUE_NR_23

## Syntax

```
VIDEO_INTERUPT_VALUE_NR_23 = $23
```

## Description

**VIDEO LINE INTERRUPT VALUE REGISTER**

More info : https://wiki.specnext.dev/Video_Line_Interrupt_Value_Register

Holds the eight LSBs of the line on which a raster interrupt should occur.

bits 7:0 = Line Interrupt value LSB (soft reset = 0)

Since core 3.1.5 the numbering of lines can be offset by Vertical Video Line Offset Register ($64).

Requires: 

	#INCLUDE <nextlib.bas>
