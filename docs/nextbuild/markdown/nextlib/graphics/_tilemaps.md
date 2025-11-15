# Tilemap

## Notice 

This page is a work in progress. It is not complete and may contain errors. For now, please refer to [https://wiki.specnext.dev/Tilemap](https://wiki.specnext.dev/Tilemap) for more information.

## Overview

The Tilemap is a hardware-accelerated character-based display mode for the ZX Spectrum Next that provides a fast way to display backgrounds, game maps, or text. It offers higher resolution than the standard ULA mode and supports color attributes without the classic attribute clash limitations.

## Specifications

The Tilemap provides:

- Two resolution modes: 40×32 (320×256 pixels) or 80×32 (640×256 pixels)
- 16-color tiles (4-bit color per pixel) or monochrome text mode
- Hardware scrolling in both X and Y directions
- Tile rotation and mirroring capabilities
- Support for up to 512 unique tiles
- Two independent palettes
- Transparent color support
- Independent control of display priority relative to other layers

The visible display area overlaps the standard ULA 256×192 area by 32 pixels on all sides. When using HDMI output, the top and bottom character rows may be cut off, making the visible area effectively 40×30 or 80×30.

## Memory Organization

The Tilemap system uses two data structures, both located in bank 5 (and optionally the first half of bank 7):

1. **Tile Definitions**: Contains the graphical data for each tile
   - Each standard tile is 32 bytes (8×8 pixels with 4 bits per pixel)
   - In text mode, each tile needs only 8 bytes (1 bit per pixel, like UDG characters)

2. **Tilemap**: Contains the map data specifying which tiles appear in which positions
   - Each entry in the tilemap is normally 2 bytes (tile number + attributes)
   - Can be configured to use 1 byte per entry (tile number only) with global attributes

## Enabling the Tilemap

To enable and configure the Tilemap, use the Tilemap Control Register (NR $6B):

```
bit 7: 0=disable tilemap, 1=enable tilemap
bit 6: 0=40×32 resolution, 1=80×32 resolution
bit 5: 0=attributes in tilemap, 1=no attributes in tilemap (use global)
bit 4: 0=primary palette, 1=secondary palette
bit 3: 0=normal mode, 1=text mode (8 bytes per tile, monochrome)
bit 2: Reserved, must be 0
bit 1: 0=256 tile mode, 1=512 tile mode
bit 0: 0=normal priority, 1=tilemap over ULA
```

Example:
```
; Enable tilemap, 40×32 resolution with attributes
NextReg $6B, %10000000

; Enable tilemap, 80×32 resolution with global attributes
NextReg $6B, %11100000

; Enable tilemap in text mode with 512 tiles
NextReg $6B, %10001010
```

## Setting Tile Data Locations

Two registers define where the tilemap data and tile definitions are stored:

### Tilemap Base Address Register (NR $6E)

```
bits 7-6: Reserved, must be 0
bits 5-0: MSB of address of the tilemap in Bank 5
```

If bit 7 is set (using NextReg $6E, 128+value), the tilemap is located in the first half of bank 7 instead of bank 5.

### Tile Definitions Base Address Register (NR $6F)

```
bits 7-6: Reserved, must be 0
bits 5-0: MSB of address of tile definitions in Bank 5
```

Example:
```
; Set tilemap base address to $6000 in bank 5
NextReg $6E, $60

; Set tile definitions to start at $4000 in bank 5
NextReg $6F, $40

; Set tilemap base address to $2000 in bank 7
NextReg $6E, $20 | %10000000
```

## Tile Attributes

Each tile in the tilemap can have attributes that modify its appearance. When attributes are used (bit 5 of NR $6B is 0), each tilemap entry consists of two bytes:

1. Tile number (0-255 or 0-511 in 512-tile mode)
2. Attribute byte:

```
bits 7-4: Palette offset
bit 3: Mirror X (horizontal flip)
bit 2: Mirror Y (vertical flip) 
bit 1: Rotate
bit 0: ULA over tilemap (in 256-tile mode) or bit 8 of tile number (in 512-tile mode)
```

In text mode, the attributes change:
```
bits 7-1: Palette offset (0-127)
bit 0: ULA over tilemap or bit 8 of tile number
```

If global attributes are enabled (bit 5 of NR $6B is 1), all tiles use the same attributes from the Default Tilemap Attribute Register (NR $6C):

```
bits 7-4: Palette offset
bit 3: Mirror X
bit 2: Mirror Y
bit 1: Rotate
bit 0: ULA over tilemap (or bit 8 of tile number in 512-tile mode)
```

Example:
```
; Set default tile attributes:
; - Palette offset 2
; - X mirroring enabled
; - No Y mirroring
; - No rotation
; - ULA over tilemap
NextReg $6C, %00101001
```

## Transparency and Clipping

### Tilemap Transparency Index Register (NR $4C)

Sets which color index (0-15) is treated as transparent, allowing background layers to show through:

```
bits 7-4: Reserved, must be 0
bits 3-0: Transparency index (default is $F)
```

### Clip Window Tilemap Register (NR $1B)

Defines a rectangular clipping window for the tilemap. Requires four consecutive writes:

```
1st write: X1 position (left)
2nd write: X2 position (right)
3rd write: Y1 position (top)
4th write: Y2 position (bottom)
```

The origin (0,0) of the clip window is the top-left corner of the full tilemap area, which is 32 pixels above and to the left of the standard ULA display area.

Example:
```
; Set transparency color to index 0
NextReg $4C, $00

; Set clip window to match ULA display area (32,32 to 32+256,32+192)
NextReg $1B, 32    ; X1 = 32
NextReg $1B, 287   ; X2 = 32+255
NextReg $1B, 32    ; Y1 = 32
NextReg $1B, 223   ; Y2 = 32+191
```

## Hardware Scrolling

The tilemap supports hardware scrolling through three registers:

### Tilemap Offset X MSB Register (NR $2F)

```
bits 7-2: Reserved, must be 0
bits 1-0: MSB of X Offset (meaningful range is 0-319 in 40-char mode, 0-639 in 80-char mode)
```

### Tilemap Offset X LSB Register (NR $30)

```
bits 7-0: LSB X Offset (meaningful range is 0-319 in 40-char mode, 0-639 in 80-char mode)
```

### Tilemap Offset Y Register (NR $31)

```
bits 7-0: Y Offset (0-255)
```

Example:
```
; Scroll tilemap 48 pixels right and 24 pixels down
NextReg $2F, 0        ; X offset MSB = 0
NextReg $30, 48       ; X offset LSB = 48
NextReg $31, 24       ; Y offset = 24

; Scroll to X position 320 (requires MSB to be set)
NextReg $2F, %00000001 ; X offset MSB = 1
NextReg $30, 64        ; X offset LSB = 64 (320 = 256 + 64)
```

## Palette Control

The tilemap has its own pair of palettes, each with 256 entries. Select which palette to write to using the Enhanced ULA Control Register (NR $43):

```
bit 7: 1=disable palette auto-increment, 0=enable
bits 6-4: Select palette:
    011 = Tilemap first palette
    111 = Tilemap second palette
bits 3-0: Other settings (not related to Tilemap)
```

Once selected, use Palette Index Register (NR $40) to select a palette entry, then write the color value using either:

- Palette Value Register (NR $41) for 8-bit RRRGGGBB format
- Enhanced ULA Palette Extension (NR $44) for 9-bit RRRGGGBBB format

Example:
```
; Select the first Tilemap palette for writing
NextReg $43, %00000011

; Set entry 0 to bright red (RRRGGGBB format)
NextReg $40, 0       ; Select palette index 0
NextReg $41, %11100000 ; Bright red color

; Set entry 1 to bright green
NextReg $40, 1
NextReg $41, %00011100
```

## Example: Basic Tilemap Setup

Here's a complete example showing how to set up a basic tilemap:

```
; 1. Initialize tilemap system
NextReg $6B, %10000000    ; Enable tilemap, 40×32, with attributes

; 2. Set up memory locations
NextReg $6E, $60          ; Tilemap data at $6000 in bank 5
NextReg $6F, $40          ; Tile definitions at $4000 in bank 5

; 3. Set default attributes (if needed)
NextReg $6C, %00000000    ; Default attributes: no flips, rotations, etc.

; 4. Set transparency color
NextReg $4C, $0F          ; Set transparency to color index 15

; 5. Select palette for configuration
NextReg $43, %00000011    ; Select first tilemap palette, auto-increment on

; 6. Set up a few palette entries
NextReg $40, 0            ; Start with palette index 0
NextReg $41, %00000000    ; Black
NextReg $41, %11100000    ; Red
NextReg $41, %00011100    ; Green
NextReg $41, %11111100    ; Yellow

; 7. Optional: Set initial scroll position
NextReg $2F, 0
NextReg $30, 0
NextReg $31, 0
```

## Example: Smooth Scrolling a Tilemap

The following example shows how to implement smooth scrolling for a tilemap:

```
; Start with tilemap scrolled to position (0,0)
NextReg $2F, 0
NextReg $30, 0
NextReg $31, 0

; Scroll right by increments of 1 pixel
scroll_right:
    ; Read current X LSB
    NextReg $30, 0        ; Select register $30 for reading
    in a, ($253B)         ; Read current value
    inc a                 ; Increment by 1
    NextReg $30, a        ; Write back the new value
    
    ; Check if we've reached 255
    cp 255
    jr nz, scroll_done
    
    ; If we hit 255, increment the MSB
    NextReg $2F, 0        ; Select register $2F for reading
    in a, ($253B)         ; Read current value
    inc a                 ; Increment by 1
    and %00000011         ; Ensure only bits 1-0 are affected
    NextReg $2F, a        ; Write back the new value

scroll_done:
    ; Continue with other code
```

## Example: Creating a Text Display Using Tilemap Text Mode

This example shows how to use the Tilemap in text mode:

```
; Set up tilemap in text mode
NextReg $6B, %10001000    ; Enable tilemap, 40×32, text mode

; Set up memory locations
NextReg $6E, $60          ; Tilemap at $6000 in bank 5
NextReg $6F, $40          ; Tile definitions at $4000 in bank 5

; Set palette for text mode (text uses entry 0 for paper, entry 1 for ink)
NextReg $43, %00000011    ; Select first tilemap palette
NextReg $40, 0            ; Select palette index 0
NextReg $41, %00000000    ; Black paper
NextReg $40, 1            ; Select palette index 1
NextReg $41, %11111100    ; Yellow ink

; After this, you would need to upload your character set to tile definitions
; and populate the tilemap with character codes
```

## Advanced Techniques

### 512-Tile Mode

To use 512 unique tiles instead of 256:

```
; Enable 512-tile mode
NextReg $6B, %10000010    ; Enable tilemap with 512-tile mode

; For tiles 0-255, bit 0 of the attribute byte should be 0
; For tiles 256-511, bit 0 of the attribute byte should be 1
```

### Stencil Mode

When both ULA and Tilemap are enabled, you can use stencil mode for special effects:

```
; Enable stencil mode in ULA Control Register
NextReg $68, %00000001    ; Bit 0 = enable stencil mode
```

In stencil mode, a pixel is transparent if both ULA and Tilemap pixels are transparent. Otherwise, the final pixel is an AND of both colors, allowing one layer to act as a cut-out for the other.

## Remarks

- The Tilemap is tied to the ULA display timing, so it works seamlessly with the standard ULA screen.
- Unlike the ULA, the Tilemap doesn't suffer from attribute clash as each pixel can have its own color.
- NextBASIC doesn't currently have native commands for the hardware Tilemap, but you can control it using NextReg commands.
- For best performance, keep tile definitions and tilemap data in bank 5 or 7 where the hardware can access them directly.
- Text mode can be useful for fast text displays without the limitations of the standard ULA character display.

## See also

* [NextReg](nextreg.md)
* [Tilemap Control Register ($6B)](tilemap_control_register_nr_6b.md)
* [Default Tilemap Attribute Register ($6C)](default_tilemap_attribute_register_nr_6c.md)
* [Tilemap Base Address Register ($6E)](tilemap_base_address_register_nr_6e.md)
* [Tile Definitions Base Address Register ($6F)](tile_definitions_base_address_register_nr_6f.md)
* [Clip Window Tilemap Register ($1B)](clip_window_tilemap_register_nr_1b.md)
* [Tilemap Offset X MSB Register ($2F)](tilemap_offset_x_msb_register_nr_2f.md)
* [Tilemap Offset X LSB Register ($30)](tilemap_offset_x_lsb_register_nr_30.md)
* [Tilemap Offset Y Register ($31)](tilemap_offset_y_register_nr_31.md)
* [Tilemap Transparency Index Register ($4C)](tilemap_transparency_index_register_nr_4c.md)
* [Layer 2](layer_2.md)
* [Sprites](sprites.md)
* [Palettes](palettes.md)
