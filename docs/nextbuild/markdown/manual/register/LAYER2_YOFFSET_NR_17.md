# LAYER2_YOFFSET_NR_17

## Syntax

```
LAYER2_YOFFSET_NR_17 = $17
```

## Description

**LAYER 2 Y OFFSET REGISTER** More info : https://wiki.specnext.dev/Layer_2_Y_Offset_Register

Sets the Y offset used when drawing Layer 2 graphics on the screen.

Layer 2 Y-offset (0 after a reset)

**Valid Range**

	0-191	'in 256x192 mode
	0-255	'0-255 in 320x256 and 640x256 modes

Requires: 

	#INCLUDE <nextlib.bas>
