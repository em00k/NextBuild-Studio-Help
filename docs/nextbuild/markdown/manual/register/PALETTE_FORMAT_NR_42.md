# PALETTE_FORMAT_NR_42

## Syntax

```
PALETTE_FORMAT_NR_42 = $42
```

## Description

**ENHANCED ULA INK COLOR MASK** (R/W)

More info : https://wiki.specnext.dev/Enhanced_ULA_Ink_Color_Mask

Specifies mask to extract ink colour from attribute cell value in ULANext mode.

Bits 7-0 = Number of the last ink colour entry in palette (core 2.0: 15 after a Reset | core 3.0: 7 after a Reset).

This number can be 1, 3, 7, 15, 31, 63, 127 or 255.

This value is used only when ULANext mode is enabled.

The 255 value enables the full ink colour mode and all the palette entries are inks. The paper and border colour is then taken from Transparency colour fallback Register ($4A).

If the ink mask is not 255, then the zeroed part of mask signals which bits will be used to extract index of paper colour. Then this index is added to 128 and read from current palette (border index is also 128 + 0..7 value from port $FE). There are no "flash" or "bright" bits when ULANext mode is enabled, all eight attribute bits contribute either to ink or paper colour index.

Applies only to Enhanced ULA palette. Layer 2, Sprite and Tilemap palettes work as "full ink" or specifically to 4-bit graphics data.

When set to "invalid" value, the ink value is masked by the value and background colour is taken from transparency fallback (as in "full ink" mode).



Requires: 

	#INCLUDE <nextlib.bas>
