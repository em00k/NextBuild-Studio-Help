# SPRITE_ATTR0_INC_NR_75

## Syntax

```
SPRITE_ATTR0_INC_NR_75 = $75
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 0 (WITH INC) REGISTER** (W)

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_0_(with_INC)_Register

Same as Sprite port-mirror Attribute 0 Register ($35) (write first byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34)

Eight low bits of X position. MSB of X-pos is in "byte 3".

After write into sprite-attribute "byte 1" (Sprite Attribute Upload ($xx57 / 87)), the Sprite port-mirror Index Register ($34) is incremented (with all consequences stemming from such action). If the sprite 127 was modified, the result of the increment is officially "undefined behaviour", and code should explicitly set valid 0..127 sprite index before next sprite-attribute manipulation.  

Requires: 

	#INCLUDE <nextlib.bas>
