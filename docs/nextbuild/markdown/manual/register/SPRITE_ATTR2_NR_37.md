# SPRITE_ATTR2_NR_37

## Syntax

```
SPRITE_ATTR2_NR_37 = $37
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 2 REGISTER**

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_2_Register

Nextreg port-mirror to write directly into "byte 3" of Sprite Attribute Upload ($xx57 / 87).

Byte 3 is bitmapped

**Bit**

	4-7  'Palette offset, added to each palette index from pattern before drawing
	3	'Enable X mirror
	2	'Enable Y mirror
	1	'Enable rotation
	0	'anchor sprite: MSB of X coordinate
		' relative sprite: enable relative Palette offset (1 = the anchor Palette offset is added, 0 = independent Palette offset)

Requires: 

	#INCLUDE <nextlib.bas>
