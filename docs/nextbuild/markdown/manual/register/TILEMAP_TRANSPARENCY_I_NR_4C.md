# TILEMAP_TRANSPARENCY_I_NR_4C

## Syntax

```
TILEMAP_TRANSPARENCY_I_NR_4C = $4C
```

## Description

**TILEMAP TRANSPARENCY INDEX REGISTER** (R/W)

More info : https://wiki.specnext.dev/Tilemap_Transparency_Index_Register

Index into Tilemap palette (of "transparent" colour).

- bits 7-4 = Reserved, must be 0
-bits 3-0 = Set the index value (0xF after reset)

The pixel index (bottom 4 bits) from tile graphics is compared before the palette offset is applied to upper 4 bits, so there is always one index of the 0-15 working as "transparent" colour.

Requires: 

	#INCLUDE <nextlib.bas>
