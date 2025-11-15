# TILEMAP_XOFFSET_LSB_NR_30

## Syntax

```
TILEMAP_XOFFSET_LSB_NR_30 = $30
```

## Description

**TILEMAP OFFSET X LSB REGISTER**

More info : https://wiki.specnext.dev/Tilemap_Offset_X_LSB_Register

Tilemap X-offset, low 8 bits of it (0 after a reset)

Meaningful Range is 0-319 in 40 char mode, 0-639 in 80 char mode.

The two top bits of the offset value are stored in Tilemap Offset X MSB Register (TILEMAP_XOFFSET_MSB_NR_2F -$2F).  

Requires: 

	#INCLUDE <nextlib.bas>
