# TILEMAP_DEFAULT_ATTR_NR_6C

## Syntax

```
TILEMAP_DEFAULT_ATTR_NR_6C = $6C
```

## Description

**DEFAULT TILEMAP ATTRIBUTE REGISTER** (R/W)

More info : https://wiki.specnext.dev/Default_Tilemap_Attribute_Register

Default tile attribute for 8-bit only maps.

**Bit**

	7-4  'Palette Offset (copied as bits 7-4 in final palette index)
	3	'X mirror
	2	'Y mirror
	1	'Rotate
	0	'If in 512-tile-mode: bit 8 of tile-id
		 'else draw priority: 1 = ULA over tilemap, 0 = tilemap over ULA

This attribute is used for all tiles if bit 5 of Tilemap Control Register ($6B) is set.

When bit 1 of Tilemap Control Register ($6B) is set, the bit 0 of tile attribute works as ninth bit of tile-id (allowing 512 tiles in total), and the priority of layers is then "ULA over Tilemap" as default.

When bit 3 of Tilemap Control Register ($6B) is set, the bits 7-1 works as Palette offset (copied to bits 7-1 in final palette index, bit 0 comes from pixel data) (there are no mirror/rotate bits in the "text mode").

Requires: 

	#INCLUDE <nextlib.bas>
