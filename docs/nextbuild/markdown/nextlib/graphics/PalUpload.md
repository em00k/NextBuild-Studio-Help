# PalUpload(address,nrOfColours,StartOffset,bank)

## Syntax

```
PalUpload(address,nrOfColours,StartOffset,bank)
```

## Description

Uploads a 9-bit palette (2 bytes per colour) to the selected palette. The palette to upload to can be selected before you call the command like so
```
NextReg($43,%00010000) : REM palette select register for Layer2 first palette
PalUpload(@palette,0,0) : REM upload from label "palette", 0 = full 256 colours, starting at index 0
DO : LOOP : REM loop forever
palette:
asm
	incbin "pal1.nxp"
end asm
```
The palette select register is as follows https://wiki.specnext.dev/Enhanced_ULA_Control_Register

	Bit
	7		1 to disable palette index write auto-increment
	6-4		Select palette for writing
	3		Selects Sprites palette (0=first,1 second)
	2		Selects Layer 2 palette (0=first,1 second)
	0		Enable ULANext mode if 1

Bits 6-4

	%000	ULA first
	%100	ULA second
	%001	Layer 2 first
	%101	Layer 2 second
	%010	Sprites first
	%110	Sprites Second
	%011	Tilemap first
	%111	Tilemap second

**Remarks**

Requires: 

	#INCLUDE <nextlib.bas>
