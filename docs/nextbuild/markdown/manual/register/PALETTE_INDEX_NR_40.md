# PALETTE_INDEX_NR_40

## Syntax

```
PALETTE_INDEX_NR_40 = $40
```

## Description

**PALETTE INDEX REGISTER** (R/W)

More info : https://wiki.specnext.dev/Palette_Index_Register

Chooses an palette element (index) to manipulate with

This associates selected element (0-255) of currently selected (Register $43) palette to be accessible through the Palette Value Register ($41) and Enhanced ULA Palette Extension ($44). Write will also reset the index of Enhanced ULA Palette Extension ($44), so the next write there will be considered as first byte of colour.

For the [classic] ULA only:
- INKs are mapped to indices 0-7
- Bright INKS are mapped to indices 8-15
- PAPERs are mapped to indices 16-23
- Bright PAPERs are mapped to indices 24-31

In ULANext mode, enabled via Enhanced ULA Control Register ($43):

- INKs come from a subset of indices 0-127 (except full-ink colour mode, when all 0-255 indices are INK colour)
- PAPERs come from a subset of indices 128-255 (in full-ink colour mode the PAPER and BORDER colour is taken from Transparency colour fallback Register ($4A))
- The number of active indices depends on the number of attribute bits assigned to INK and PAPER out of the attribute byte by Enhanced ULA Ink Color Mask ($42).

In ULA+ mode, the top 64 entries hold the ULA+ palette.

The ULA always takes border colour from paper colours.

Layer 2, Sprite and LoRes palettes work as "full ink" always, INK/PAPER concept does apply only to classic/enhanced ULA palette.

The Tilemap palette contains 256 colours, but number of colour selected by particular pixel of tile consists of top 4 bits from tile attribute and bottom 4 bits from the tile pixel, i.e. the Tilemap palette works like 16x16 sub-palettes, with each tile being defined with 0-15 indices only (and one index of them is transparent). Then the attribute of the tile fills up the top four bits, selecting 0-15 "sub-palette".

4-bit sprites test for transparency only against low 4 bits of Sprite transparency register, and further the pixels are processed similarly to 8-bit sprites, as if the top 4 bits in pattern data were all zeroes. I.e. to the pixel value the palette offset from sprite attributes is added, and final index is used to fetch colour from Sprite palette. Transparency index is compared before the palette offset is applied.

Requires: 

	#INCLUDE <nextlib.bas>
