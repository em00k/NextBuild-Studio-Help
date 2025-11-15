# TILEMAP_CONTROL_NR_6B

## Syntax

```
TILEMAP_CONTROL_NR_6B = $6B
```

## Description

**TILEMAP CONTROL REGISTER** (R/W)

More info : https://wiki.specnext.dev/Tilemap_Control_Register

Controls [Tilemap](https://wiki.specnext.dev/Tilemap) mode.

**Bit**

	7	'1 to enable the tilemap
	6	'0 for 40x32, 1 for 80x32
	5	'1 to eliminate the attribute entry in the tilemap
	4	'palette select (0 tilemap first, 1 second)
	3	'enable "text" mode
	2	'Reserved : must be 0
	1	'1 to activate 512 tile mode (bit 0 of tile attribute is ninth bit of tile-id)
		 '0 to use bit 0 of tile attribute as "ULA over tilemap" per-tile-selector
	0	'1 to enforce "tilemap over ULA" layer priority

Bits 7 & 6 enable the tilemap and select resolution.

Bit 5 changes the structure of the tilemap so that it contains only 8-bit tilemap-id entries instead of 16-bit tilemap-id plus tile-attribute entries.

If 8-bit tilemap is selected, the tilemap contains only tile numbers and the attributes are taken from Default Tilemap Attribute Register ($6C).

Bit 4 selects one of two tilemap palettes used for final colour lookup.

Bit 3 enables "text mode" where the tile-graphic is defined as 1-bit B&W bitmap (same as UDG = User Defined Graphic characters on original ZX Spectrum) => one tile needs only 8 bytes to define graphics. The tile-map data are also interpreted differently, the associated flag byte is 7:1 split, the bottom bit 0 being still "ULA over Tilemap" or "ninth bit of tile number", but the top 7 bits are extended palette offset (copied as top 7 bits of palette index, the eight bottom bit is the pixel value). The transparency is then checked against the Global Transparency Register ($14) colour (after the colour lookup in the palette), not against the four bit Tilemap transparency colour-index.

Bit 1 enables the 512-tile-mode when the tile attribute (either global in Default Tilemap Attribute Register ($6C) or per tile in map data) contains ninth bit of tile-id value. In this mode the tiles are drawn under ULA pixels, unless bit 0 is used to force whole Tilemap over ULA.

Bit 0 can enforce Tilemap over ULA either in 512-tile-mode, or even override the per-tile bit selector from tile attributes. If zero, the Tilemap priority is either decided by attribute bit or in 512-tile-mode it is under ULA.   

Requires: 

	#INCLUDE <nextlib.bas>
