# LAYER2_XOFFSET_NR_16

## Syntax

```
LAYER2_XOFFSET_NR_16 = $16
```

## Description

**LAYER 2 X OFFSET REGISTER** More info : https://wiki.specnext.dev/Layer_2_X_Offset_Register

Sets the pixel offset used for drawing Layer 2 graphics on the screen.

**Valid Range**

	0-255	'0 after a reset

The ninth most significant bit of scroll value is in **Layer 2 X Offset MSB Register** ($71) (for the 320x256 and 640x256 modes the valid X-offset range is 0..319, so one more bit is needed).

Requires: 

	#INCLUDE <nextlib.bas>
