# SPRITE_ATTR3_INC_NR_78

## Syntax

```
SPRITE_ATTR3_INC_NR_78 = $78
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 3 (WITH INC) REGISTER** (W)

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_3_(with_INC)_Register

Same as Sprite port-mirror Attribute 3 Register ($38) (write fourth byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34)

Byte 4 is bitmapped:

**Bit**

	7	'Enable visibility
	6	'Enable fifth sprite attribute byte
	5-0  'Pattern index ("Name")

When the bit 6 is "0", the sprite renderer will ignore value written in fifth attribute byte, for example by Sprite port-mirror Attribute 4 Register ($39), and it will use zero for all the features of fifth attribute byte (it is safe to initialize only four bytes if you are planning to use 4-byte type of sprites).

If you want the value in fifth attribute byte to apply during rendering, bit 6 here must be set to "1".

After write into sprite-attribute "byte 4" (Sprite Attribute Upload ($xx57 / 87)), the Sprite port-mirror Index Register ($34) is incremented (with all consequences stemming from such action). If the sprite 127 was modified, the result of the increment is officially "undefined behaviour", and code should explicitly set valid 0..127 sprite index before next sprite-attribute manipulation.

Requires: 

	#INCLUDE <nextlib.bas>
