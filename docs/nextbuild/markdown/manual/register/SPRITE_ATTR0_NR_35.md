# SPRITE_ATTR0_NR_35

## Syntax

```
SPRITE_ATTR0_NR_35 = $35
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 0 REGISTER** (W)

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_0_Register

Nextreg port-mirror to write directly into "byte 1" of Sprite Attribute Upload ($xx57 / 87).

Eight low bits of X position. MSB of X-pos is in "byte 3".

Requires: 

	#INCLUDE <nextlib.bas>
