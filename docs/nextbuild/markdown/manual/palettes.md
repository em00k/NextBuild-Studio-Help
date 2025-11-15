# Palettes

## Overview

The ZX Spectrum Next supports an advanced palette system that significantly expands the color capabilities beyond the original ZX Spectrum's 15 colors. The palette system allows different graphics modes to access various color options through a series of palette registers and indices.

## Color Basics

The ZX Spectrum Next uses a 9-bit color system (RRRGGGBBB), allowing for a total of 512 possible colors. Each color component (Red, Green, Blue) uses 3 bits, providing 8 levels of intensity (0-7) per component.

```
RRRGGGBB,B format:
R = Red bits (0-7)
G = Green bits (0-7) 
B = Blue bits (0-7)
```

Colors can be specified using 8-bit (RRRGGGBB) or 9-bit (RRRGGGBBB) values. When using 8-bit values, the missing blue bit is automatically generated as a logical OR of the two existing blue bits.

## Supported Modes

The number of displayable colors varies depending on the graphics mode:

* **Standard ULA**: 15 colors on screen at once (7 colors plus bright variations, as bright black is still black), using 1 of 2 ULA palettes
* **ULANext**: Up to 256 colors via attribute mapping, using 1 of 2 ULA Next palettes
* **Sprites**: 16 colors per sprite (4-bit) with palette offsets or 256 colors (8-bit), using 1 of 2 sprite palettes
* **Layer 2**: Full 256-color display, using 8-bit pixel values as palette indices, using 1 of 2 Layer 2 palettes
* **Tilemap**: Up to 16 colors per tile using one of two tilemap palettes for final color lookup

## Setting Palette Colors

To define a color in a palette:

1. Use [Enhanced ULA Control Register (NR $43)](PALETTE_CONTROL_NR_43.md) to select which palette to write to
2. Use [Palette Index Register (NR $40)](PALETTE_INDEX_NR_40.md) to select the palette entry index
3. Then send the color using either:
   * [Palette Value Register (NR $41)](PALETTE_VALUE_NR_41.md) to send an 8-bit color in RRRGGGBB format
   * [Enhanced ULA Palette Extension (NR $44)](PALETTE_VALUE_9BIT_NR_44.md) to send a 9-bit color, as two bytes

## Palette Registers

### Palette Index Register (NR $40)

```
bits 7-0 = Select the palette index to modify
```

This register selects which color index in the current palette will be modified. The palette is selected via the Enhanced ULA Control Register (NR $43).

For the ULA, palette indices have special meanings:
* Standard INK = indices 0-7
* Bright INK = indices 8-15
* PAPER = indices 16-23
* Bright PAPER = indices 24-31

In ULANext mode, INK uses indices 0-127 and PAPER uses indices 128-255. In ULA+ mode, the top 64 entries hold the ULA+ palette.

### Palette Value Register (NR $41)

```
bits 7-0 = 8-bit color value in RRRGGGBB format
```

This register writes an 8-bit color value to the index selected by the Palette Index Register (NR $40). The missing third blue bit is automatically generated as an OR of the two blue bits. After each write, the index is auto-incremented if auto-increment is enabled in register NR $43.

### Enhanced ULA Ink Color Mask (NR $42)

```
bits 7-0 = Mask for ULANext attribute format
```

Defines how many bits of the ULA attribute byte represent INK (the rest is PAPER). Must be one of: 1, 3, 7, 15, 31, 63, 127, or 255. If the mask is 255 (full ink), PAPER and BORDER colors come from the fallback color in NR $4A.

### Enhanced ULA Control Register (NR $43)

```
bit 7    = Disable auto-increment (1 = disabled)
bits 6-4 = Select palette to write or read:
           000 = ULA first palette
           100 = ULA second palette
           001 = Layer 2 first palette
           101 = Layer 2 second palette
           010 = Sprites first palette
           110 = Sprites second palette
           011 = Tilemap first palette
           111 = Tilemap second palette
bit 3    = Select Sprites palette (0 = first, 1 = second)
bit 2    = Select Layer 2 palette (0 = first, 1 = second)
bit 1    = Select ULA palette (0 = first, 1 = second)
bit 0    = Enable ULANext mode (0 after reset)
```

This register controls palette selection, auto-increment behavior, and enables ULANext mode.

### Enhanced ULA Palette Extension (NR $44)

```
First byte:  RRRGGGBB
Second byte: P000000B
             bit 0 = LSB of blue component
             bit 7 = Layer 2 priority (if 1, Layer 2 pixel appears above all other layers)
```

This register requires two consecutive writes to set a 9-bit color. For Layer 2, bit 7 of the second byte determines priority.

### Transparency Color Fallback Register (NR $4A)

```
bits 7-0 = 8-bit fallback color (RRRGGGBB)
```

This 8-bit color is used when all layers are transparent. It's also used as PAPER/BORDER color when ULANext attribute mask is invalid or set to 255.

### Sprites Transparency Index Register (NR $4B)

```
bits 7-0 = Transparency index for sprites
```

Sets which palette index will be treated as transparent in sprite rendering. For 4-bit sprites, only the bottom 4 bits are used.

### Tilemap Transparency Index Register (NR $4C)

```
bits 7-4 = Reserved, must be 0
bits 3-0 = Transparency index for tilemap
```

Sets which palette index (0-15) will be treated as transparent for tilemap rendering.

## Working with Palettes

### ULA and ULANext Modes

In standard ULA mode, the color mapping follows the classic ZX Spectrum model:
* INK: palette indices 0-7
* BRIGHT INK: indices 8-15
* PAPER and BORDER: indices 16-23 and 24-31

In ULANext mode (enabled via bit 0 of NR $43), the attribute byte is split differently:
* INK: indices 0-127
* PAPER/BORDER: indices 128-255
* The mask in NR $42 defines how the attribute byte is split into INK and PAPER

### Layer 2 Priority Colors

Layer 2 colors can have a priority bit set (bit 7 in the second byte of NR $44). When this bit is set, the Layer 2 pixel will be drawn above all other layers, regardless of the layer priority settings. If you need the same color in both priority and non-priority versions, you'll need two different palette entries.

## Available Files

Various palette files are available in different formats:
* Adobe Photoshop (.ACT)
* GIMP (.GPL)
* JASC (.PAL)
* Raw binary formats


## Remarks

* Modern displays use 8-bit RGB values (0-255), but the Spectrum Next uses 3-bit values (0-7), so converting colors will always involve some form of approximation.
* Only 256 colors can be displayed at once, even when using 512-color palettes.
* Auto-increment of the palette index can be disabled by setting bit 7 of NR $43.
* ULA+ mode is available by enabling bit 3 of ULA Control Register ($68) for compatibility with ULA+ systems.

## See also

* [Palette Index Register (NR $40)](PALETTE_INDEX_NR_40.md)
* [Palette Value Register (NR $41)](PALETTE_VALUE_NR_41.md)
* [Enhanced ULA Ink Color Mask (NR $42)](PALETTE_FORMAT_NR_42.md)
* [Enhanced ULA Control Register (NR $43)](PALETTE_CONTROL_NR_43.md)
* [Enhanced ULA Palette Extension (NR $44)](PALETTE_VALUE_9BIT_NR_44.md)
* [Transparency Color Fallback Register (NR $4A)](transparency_color_fallback_register_nr_4a.md)
* [Sprites Transparency Index Register (NR $4B)](sprites_transparency_index_register_nr_4b.md)
* [Tilemap Transparency Index Register (NR $4C)](tilemap_transparency_index_register_nr_4c.md)
* [Layer 2](layer_2.md)
* [Sprites](_sprites.md)
* [Tilemap](tilemap.md)
