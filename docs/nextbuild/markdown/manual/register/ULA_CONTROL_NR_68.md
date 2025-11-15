# ULA_CONTROL_NR_68

## Syntax

```
ULA_CONTROL_NR_68 = $68
```

## Description

**ULA CONTROL REGISTER** (R/W)

More info : https://wiki.specnext.dev/ULA_Control_Register

Disable ULA, controls ULA mixing/blending, enable ULA+

**Bit**

	7	' 1 to disable ULA output (soft reset = 0)
	6-5  ' %00 for ULA as BLEND colour
		 ' %10 for ULA/tilemap as BLEND colour
		 ' %11 for tilemap as BLEND colour
		 ' %01 for no blending
	4	' Cancel entries in 8x5 matrix for extended keys
	3	' ULA+ enable (soft reset = 0)
	2	' may change (ULA half pixel scroll) (soft reset = 0)
	1	' Reserved, must be 0
	0	' 1 to enable stencil mode when both the ULA and tilemap are enabled
		 ' (if either are transparent the result is transparent otherwise the result is a logical AND of both colours)

Bit 0 can be set to choose stencil mode for the combined output of the ULA and [Tilemap](https://wiki.specnext.dev/Tilemap).

Bits 6-5 determine what colour is used in SLU modes 6 & 7 where the ULA is combined with Layer 2 to generate highlighting effects []Sprite and Layers System Register ($15)](https://wiki.specnext.dev/Sprite_and_Layers_System_Register).

Requires: 

	#INCLUDE <nextlib.bas>
