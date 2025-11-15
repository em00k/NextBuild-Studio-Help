# PALETTE_VALUE_NR_41

## Syntax

```
PALETTE_VALUE_NR_41 = $41
```

## Description

**PALETTE VALUE REGISTER** (R/W)

More info : https://wiki.specnext.dev/Palette_Value_Register

Use to set/read 8-bit colours of the ULANext palette.

Bits 7-0 = Eight bit colour for the palette index selected by the Palette Index Register ($40).

Format is **RRRGGGBB** - Note the lowest blue bit of colour (*ninth bit*) will be set to an *OR* between bit 1 and bit 0.

After the write, the palette index is auto-incremented to the next index, if the auto-increment is enabled at *Enhanced ULA Control Register* ($43). And also the index of *Enhanced ULA Palette Extension* ($44) is reset, so the next write there will be considered as first byte of colour.

Read does not auto-increment the index, and reads always the top 8 bits of colour from palette, to read the 9th bit of colour, use *Enhanced ULA Palette Extension* ($44) in tandem with value from this register.

The modified palette remains until a Hard Reset.

Requires: 

	#INCLUDE <nextlib.bas>
