# SPRITE_ATTR4_INC_NR_79

## Syntax

```
SPRITE_ATTR4_INC_NR_79 = $79
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 4 (WITH INC) REGISTER** (W)

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_4_(with_INC)_Register

The same as Sprite port-mirror Attribute 4 Register ($39) (write fifth byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34)

Byte 5 is mitmapped.

*For Anchor sprites:*

**Bits**

	7-6  '"H N6" - "H" is 4/8 bit graphics selector, "N6" is sub-pattern selector for 4 bit modes.
		 %00 ' 8-bit colour patterns (256 bytes), this sprite is "anchor"
		 %01 ' this sprite is "relative" (4/8-bit colour is selected by "anchor" sprite) → see tables below
		 %10 ' 4-bit colour pattern (128 bytes) using bytes 0..127 of pattern slot, this sprite is "anchor"
		 %11 ' 4-bit colour pattern (128 bytes) using bytes 128..255 of pattern slot, this sprite is "anchor"
	5	'Type for following relative sprites: 0 = "composite", 1 = "big sprite"
	4-3  'x-axis scale factor: %00 = 1x (16 pixels), %01 = 2x, %10 = 4x, %11 = 8x (128 pixels)
	2-1  'y-axis scale factor: %00 = 1x (16 pixels), %01 = 2x, %10 = 4x, %11 = 8x (128 pixels)
	0	'MSB of Y coordinate

*For Anchor sprites:*

**Bits**

	7-6  %01 ' relative sprite
	5	'"N6" bit, in 4-bit colour mode 0 = using bytes 0..127 of pattern slot, 1 = using bytes 128..255 of pattern slot. In 8-bit mode use 0.
	4-3  'x-axis scale factor: %00 = 1x (16 pixels), %01 = 2x, %10 = 4x, %11 = 8x (128 pixels)
	2-1  'y-axis scale factor: %00 = 1x (16 pixels), %01 = 2x, %10 = 4x, %11 = 8x (128 pixels)
	0	'Enable relative pattern offset (1 = Pattern index is added to anchor pattern index, 0 = independent pattern index)

*For big relative-sprites*

**Bit**

	7-6  %01 'relative sprite
	5	'"N6" bit, in 4-bit colour mode 0 = using bytes 0..127 of pattern slot, 1 = using bytes 128..255 of pattern slot. In 8-bit mode use 0.
	4-1  'use 0 (scaling is defined by anchor sprite)
	0	'Enable relative pattern offset (1 = Pattern index is added to anchor pattern index, 0 = independent pattern index)

See Sprite Attribute Upload ($xx57 / 87) for extra notes about anchor/relative sprites, coordinates and clipping.

After write into sprite-attribute "byte 5" [(Sprite Attribute Upload ($xx57 / 87)](https://wiki.specnext.dev/Sprite_Attribute_Upload), the Sprite port-mirror Index Register ($34) is incremented (with all consequences stemming from such action). If the sprite 127 was modified, the result of the increment is officially "undefined behaviour", and code should explicitly set valid 0..127 sprite index before next sprite-attribute manipulation.

Requires: 

	#INCLUDE <nextlib.bas>
