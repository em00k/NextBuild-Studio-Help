# CLIP_WINDOW_CONTROL_NR_1C

## Syntax

```
CLIP_WINDOW_CONTROL_NR_1C = $1C
```

## Description

**CLIP WINDOW CONTROL REGISTER**

More info : https://wiki.specnext.dev/Clip_Window_Control_Register

Controls (resets) the clip-window registers indices. (R/W)

**Bit Write**

	Bit	Function
	7-4  'Reserved must be 0
	3	'reset the Tilemap clip-window register index (by writing 1).
	2	'reset the ULA/LoRes clip-window register index (by writing 1).
	1	'reset the Sprite clip-window register index (by writing 1).
	0	'reset the Layer 2 clip-window register index (by writing 1).

**Bit Read**

	7-6  'the current Tilemap clip-window register index  
	5-4  'the current ULA/LoRes clip-window register index
	3-2  'he current Sprite clip-window register index
	1-0  'the current Layer 2 clip-window register index

Requires: 

	#INCLUDE <nextlib.bas>
