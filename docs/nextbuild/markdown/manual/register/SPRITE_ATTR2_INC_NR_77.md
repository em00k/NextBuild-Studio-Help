# SPRITE_ATTR2_INC_NR_77

## Syntax

```
SPRITE_ATTR2_INC_NR_77 = $77
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 2 (WITH INC) REGISTER** (W)

More info : hhttps://wiki.specnext.dev/Sprite_port-mirror_Attribute_2_(with_INC)_Register

Same as Sprite port-mirror Attribute 2 Register ($37) (write third byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34)

Byte 3 is bitmapped

**Bit**

	4-7  'Palette offset, added to each palette index from pattern before drawing
	3	'Enable X mirror
	2	'Enable Y mirror
	1	'Enable rotation
	0	'anchor sprite : MSB of X coordinate
		'relative sprite: enable relative Palette offset (1 = the anchor Palette offset is added, 0 = independent Palette offset)

After write into sprite-attribute "byte 3" (Sprite Attribute Upload ($xx57 / 87)), the Sprite port-mirror Index Register ($34) is incremented (with all consequences stemming from such action). If the sprite 127 was modified, the result of the increment is officially "undefined behaviour", and code should explicitly set valid 0..127 sprite index before next sprite-attribute manipulation. 

Requires: 

	#INCLUDE <nextlib.bas>
