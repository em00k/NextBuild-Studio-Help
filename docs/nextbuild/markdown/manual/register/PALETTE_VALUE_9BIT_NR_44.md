# PALETTE_VALUE_9BIT_NR_44

## Syntax

```
PALETTE_VALUE_9BIT_NR_44 = $44
```

## Description

**ENHANCED ULA PALETTE EXTENSION** (R/W)

More info : https://wiki.specnext.dev/Enhanced_ULA_Palette_Extension

Use to set 9-bit (2-byte) colours of the Enhanced ULA palette, or to read second byte of colour.

Two consecutive writes are needed to write the 9 bit colour:
- 1st write: bits 7-0 = RRRGGGBB
- 2nd write: bits 7-1 are reserved, must be 0 (except bit 7 for Layer 2), bit 0 = lsb B

```
	NextReg $43, %00010000			; 	%001 Layer2 first palette
	NextReg $40, 0 					; 	reset palette index 
	NextReg $44, $ff 				; 	9bit white 
	NextReg	$44, 01 
```

(to detect whether first or second write is expected, one can read bit 7 of Machine Type Register ($03), in case your code is not aware of current state)

If writing the Layer 2 palette colour, in the second byte, bit 7 is "priority" bit. Priority colour will be always on top (drawn above all other layers), even on a priority arrangement like "USL" . If you need the exact same colour with priority and non priority, you will need to program the same colour twice, changing bit 7 to 0 for the non priority colour alternative.

After the write of second byte, the palette index is auto-incremented, if the auto-increment is enabled by Enhanced ULA Control Register ($43).

The read will always read the second byte of colour (%p000000B) and it will not modify the index.

The modified palette remains until a Hard Reset.   

Requires: 

	#INCLUDE <nextlib.bas>
