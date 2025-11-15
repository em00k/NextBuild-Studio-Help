# PALETTE_CONTROL_NR_43

## Syntax

```
PALETTE_CONTROL_NR_43 = $43
```

## Description

**ENHANCED ULA CONTROL REGISTER** (R/W)

More info : https://wiki.specnext.dev/Enhanced_ULA_Control_Register

Enables or disables Enhanced ULA interpretation of attribute values and toggles active palette.

**Bit**

	7	 '1 to disable palette index write auto-increment
	6-4  'Select palette for reading or writing
	3	 'Select Sprites palette (0 = first palette, 1 = second palette)
	2	 'Select Layer 2 palette (0 = first palette, 1 = second palette)
	1	 'Select ULA palette (0 = first palette, 1 = second palette)
	0	 'Enable ULANext mode if 1. (0 after a reset)

n.b. Bits 6-4 select palette for reading or writing whereas bits 3-1 select the palette for the display signal generator.

Possible bits 6-4 for palette select (bit 6 selects first/second, 5-4 select type):

**Bits 6-4**
```
    %0xxx0000
	%000	ULA first palette
	%100	ULA second palette
	%001	Layer2 first palette
	%101	Layer2 second palette
	%010	Sprites first palette
	%110	Sprites second palette
	%011	Tilemap first palette
	%111	Tilemap second palette
```

Write will also reset the index of Enhanced ULA Palette Extension ($44), so the next write there will be considered as first byte of colour.

Requires: 

	#INCLUDE <nextlib.bas>
