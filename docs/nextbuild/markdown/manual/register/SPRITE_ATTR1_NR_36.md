# SPRITE_ATTR1_NR_36

## Syntax

```
SPRITE_ATTR1_NR_36 = $36
```

## Description

**SPRITE PORT-MIRROR ATTRIBUTE 1 REGISTER** (W)

More info : https://wiki.specnext.dev/Sprite_port-mirror_Attribute_1_Register

Nextreg port-mirror to write directly into "byte 2" of Sprite Attribute Upload ($xx57 / 87).

Eight low bits of Y position. MSB of Y-pos is in "byte 5". 

Requires: 

	#INCLUDE <nextlib.bas>
