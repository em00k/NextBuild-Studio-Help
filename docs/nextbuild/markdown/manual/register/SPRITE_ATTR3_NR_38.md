# SPRITE_ATTR3_NR_38

## Syntax

```
SPRITE_ATTR3_NR_38 = $38
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 3 REGISTER** (W)

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_3_Register

Nextreg port-mirror to write directly into "byte 4" of Sprite Attribute Upload($xx57 / 87).

Byte 3 is bitmapped:

**Bits**

	7	'Enable visibility
	6	'Enable fifth sprite attribute
	5-0  'Pattern index ("Name")

When the bit 6 is "0", the sprite renderer will ignore value written in fifth attribute byte, for example by Sprite port-mirror Attribute 4 Register ($39), and it will use zero for all the features of fifth attribute byte (it is safe to initialize only four bytes if you are planning to use 4-byte type of sprites).

If you want the value in fifth attribute byte to apply during rendering, bit 6 here must be set to "1".

Requires: 

	#INCLUDE <nextlib.bas>
