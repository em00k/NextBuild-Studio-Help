# SPRITE_TRANSPARENCY_I_NR_4B

## Syntax

```
SPRITE_TRANSPARENCY_I_NR_4B = $4B
```

## Description

**SPRITES TRANSPARENCY INDEX REGISTER** (R/W)

More info : https://wiki.specnext.dev/Sprites_Transparency_Index_Register

Index into sprite palette (of "transparent" colour).

Index into sprite palette, set to $E3 after reset.

When rendering sprites, the pixel index is compared before palette-offset (byte 3 of Sprite Attribute Upload ($xx57 / 87)) is applied to it. The transparency is index-based, not colour based (contrary to Layer 2/ULA/LoRes modes, where resulting pixel colour is compared).

The 4-bit sprite compares pixel-index to low 4 bits of this register, i.e. 4-bit pixel $3 (%0011) is treated as transparent, if this register still contains default $E3 (%1110_0011) value.

Requires: 

	#INCLUDE <nextlib.bas>
