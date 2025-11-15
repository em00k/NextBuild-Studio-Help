# TILEMAP_XOFFSET_MSB_NR_2F

## Syntax

```
TILEMAP_XOFFSET_MSB_NR_2F = $2F
```

## Description

**TILEMAP OFFSET X MSB REGISTER**

Sets the pixel offset (two high bits) used for drawing Tilemap graphics on the screen

**Bits

	7-2  'Reserved must be 0
	1-0  'Tilemap X-offset, top two bits of it (0 after a reset)

Meaningful Range is 0-319 in 40 char mode, 0-639 in 80 char mode.

The low eight bits of the offset value are stored in Tilemap Offset X LSB Register (TILEMAP_XOFFSET_LSB_NR_30 $30).  

More info : https://wiki.specnext.dev/Tilemap_Offset_X_MSB_Register

Requires: 

	#INCLUDE <nextlib.bas>
