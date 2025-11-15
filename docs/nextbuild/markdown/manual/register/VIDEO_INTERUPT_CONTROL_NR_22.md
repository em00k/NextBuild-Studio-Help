# VIDEO_INTERUPT_CONTROL_NR_22

## Syntax

```
VIDEO_INTERUPT_CONTROL_NR_22 = $22
```

## Description

**VIDEO LINE INTERRUPT CONTROL REGISTER**

More info : https://wiki.specnext.dev/Board_feature_control

Controls the timing of raster interrupts and the ULA frame interrupt. (R/W)

	Bit	Function
	7	'(R) INT signal (even when Z80N has interrupts disabled) (1 = interrupt is requested)
		 '(W) Reserved, must be 0
	6-3  'Reserved, must be 0 
	2	'If 1 disables original ULA interrupt (Reset to 0 after a reset)
	1	'If 1 enables Line Interrupt (Reset to 0 after a reset)
	0	'MSB of Line Interrupt line value (Reset to 0 after a reset)

The line interrupt value uses coordinate system of Copper coprocessor, i.e. line 0 is the first line of pixels. But the line-interrupt happens already when the previous line's pixel area is finished (i.e. the raster-line counter still reads "previous line" and not the one programmed for interrupt). The INT signal is raised while display beam horizontal position is between 256-319 standard pixels, precise timing of interrupt handler execution then depends on how-quickly/if the Z80 will process the INT signal.

The LSB part of desired interrupt line is in Video Line Interrupt Value Register ($23).

Since core 3.1.5 the numbering of lines can be offset by Vertical Video Line Offset Register ($64).  

Requires: 

	#INCLUDE <nextlib.bas>
