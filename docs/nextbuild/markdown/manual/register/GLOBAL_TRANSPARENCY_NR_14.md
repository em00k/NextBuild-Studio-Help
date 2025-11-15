# GLOBAL_TRANSPARENCY_NR_14

## Syntax

```
GLOBAL_TRANSPARENCY_NR_14 = $14
```

## Description

**GLOBAL TRANSPARENCY REGISTER** More info : https://wiki.specnext.dev/Global_Transparency_Register

Sets the "transparent" colour for Layer 2, ULA and LoRes pixel data.  (R/W)

Transparency color value (0xE3 after a reset).

This value is 8-bit only, so the transparency is compared only by the MSB bits of the final colour.

This only affects Layer 2, ULA, LoRes and 1-bit ("text mode") tilemap. Sprites use **SPRITE_TRANSPARENCY_I_NR_4B** ($4B) for transparency, 4-bit Tilemap uses **TILEMAP_TRANSPARENCY_I_NR_4C** ($4C). 

Requires: 

	#INCLUDE <nextlib.bas>
