# SPRITE_ATTR1_INC_NR_76

## Syntax

```
SPRITE_ATTR1_INC_NR_76 = $76
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 1 (WITH INC) REGISTER** (W)

https://wiki.specnext.dev/Sprite_port-mirror_Attribute_1_(with_INC)_Register

Same as Sprite port-mirror Attribute 1 Register ($36) (write second byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34)

Eight low bits of Y position. MSB of Y-pos is in "byte 5".

After write into sprite-attribute "byte 2" (Sprite Attribute Upload ($xx57)), the Sprite port-mirror Index Register ($34) is incremented (with all consequences stemming from such action). If the sprite 127 was modified, the result of the increment is officially "undefined behaviour", and code should explicitly set valid 0..127 sprite index before next sprite-attribute manipulation.  

Requires: 

	#INCLUDE <nextlib.bas>
