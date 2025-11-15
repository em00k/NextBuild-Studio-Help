# TRANSPARENCY_FALLBACK_COL_NR_4A

## Syntax

```
TRANSPARENCY_FALLBACK_COL_NR_4A = $4A
```

## Description

**TRANSPARENCY COLOUR FALLBACK REGISTER** (R/W)

More info : https://wiki.specnext.dev/Transparency_colour_fallback_Register

8-bit colour to be used when all layers contain transparent pixel.

Colour format is RRRGGGBB, like Palette Value Register ($41) uses.

Value is 0 (black colour) on reset.

This colour is also used for PAPER and BORDER when ULANext mode is enabled, and "full ink" (ink mask = 255) mode is selected.  

Requires: 

	#INCLUDE <nextlib.bas>
