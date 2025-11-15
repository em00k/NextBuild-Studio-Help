# ZX Spectrum Next Sprites Reference

## Table of Contents

- [Overview](#overview)
- [Sprite Characteristics](#sprite-characteristics) 
- [Sprite Patterns](#sprite-patterns)
  - [Pattern Number](#pattern-number)
  - [8-Bit Sprite Patterns](#8-bit-sprite-patterns)
  - [4-Bit Sprite Patterns](#4-bit-sprite-patterns)
  - [Sprite Palette](#sprite-palette)
- [Sprite Attributes](#sprite-attributes)
  - [Sprite Attribute 0](#sprite-attribute-0---x-coordinate-lsb)
  - [Sprite Attribute 1](#sprite-attribute-1---y-coordinate-lsb)
  - [Sprite Attribute 2](#sprite-attribute-2)
  - [Sprite Attribute 3](#sprite-attribute-3)
  - [Sprite Attribute 4](#sprite-attribute-4)
- [Relative Sprites](#relative-sprites)
  - [Composite Sprites](#composite-sprites)
  - [Unified Sprites](#unified-sprites)
- [Programming Sprites](#programming-sprites)
  - [IO Ports](#io-ports)
  - [Nextreg Interfaces](#nextreg-interfaces)
- [Global Control of Sprites](#global-control-of-sprites)

## Overview

The Spectrum Next hardware sprite system provides:
- 128 total sprites
- Display surface of 320×256 pixels
- Minimum 100 sprites per scanline
- 512 colours per pixel
- 16×16 pixel sprite size (can be magnified 2x, 4x, or 8x)
- Sprite mirroring and rotation capabilities
- Sprite grouping functionality
- 16K pattern memory for sprite images

## Sprite Characteristics

- **Total sprites**: 128
- **Display surface**: 320×256 (overlaps ULA screen by 32 pixels on each side)
- **Minimum sprites per scanline**: 100†
- **Color depth**: 512 colors per pixel
- **Sprite size**: 16×16 pixels
- **Magnification options**: 2x, 4x, or 8x horizontally and vertically
- **Features**: Can be mirrored, rotated, and grouped
- **Pattern memory**: 16K (can hold 64 8-bit or 128 4-bit sprite images)

† The actual limit depends on 28MHz clock cycles in a scanline. The hardware ensures sprites are not partially plotted.

## Sprite Patterns

### 1.1 Pattern Number

The pattern number is a 7-bit value that identifies sprite images in pattern memory:

| Bit Position | Name | Description |
|-------------|------|-------------|
| 6 | N5 | Most significant bit |
| 5 | N4 | Pattern number bit 4 |
| 4 | N3 | Pattern number bit 3 |
| 3 | N2 | Pattern number bit 2 |
| 2 | N1 | Pattern number bit 1 |
| 1 | N0 | Pattern number bit 0 |
| 0 | N6 | Least significant bit (despite the name) |

**Note**: For 8-bit sprites, N6=0 always. The remaining 6 bits can identify 64 patterns.

### 1.2 8-Bit Sprite Patterns

- Uses 8 bits per pixel (256 colors)
- Requires 256 bytes of pattern memory
- Transparent color determined by Sprite Transparency Index register (default 0xE3)

### 1.3 4-Bit Sprite Patterns

- Uses 4 bits per pixel (16 colors)
- Requires 128 bytes of pattern memory
- Two pixels stored per byte (left pixel in upper 4 bits, right pixel in lower 4 bits)
- Transparent color uses lower 4 bits of Sprite Transparency Index register (default 0x3)

### 1.4 Sprite Palette

The sprite palette system works as follows:

1. **Color Index Calculation**:

   **8-bit Sprite**:
   ```
   PPPP0000 + IIIIIIII = SSSSSSSS
   ```
   
   **4-bit Sprite**:
   ```
   PPPP0000 + 0000IIII = PPPPIIII
   ```
   
   Where:
   - PPPP = 4-bit palette offset from sprite attributes
   - I = Pixel value from sprite pattern
   - S = Final sprite index

2. The final 8-bit sprite index is passed through the sprite palette lookup table to get the 9-bit RGB333 color.

## Sprite Attributes

Each sprite is defined by 4 or 5 attribute bytes:

### Sprite Attribute 0 - X Coordinate LSB

| Bits | Description |
|------|-------------|
| 7-0 | X coordinate (bits 0-7) |

### Sprite Attribute 1 - Y Coordinate LSB

| Bits | Description |
|------|-------------|
| 7-0 | Y coordinate (bits 0-7) |

### Sprite Attribute 2

| Bit | Description |
|-----|-------------|
| 7-4 | Palette offset (4 bits) |
| 3 | X mirror |
| 2 | Y mirror |
| 1 | Rotate (90° clockwise) |
| 0 | X8/PR (9th bit of X coordinate or relative palette flag) |

**Note**: Rotation is applied before mirroring. For relative sprites, bit 0 becomes PR flag.

### Sprite Attribute 3

| Bit | Description |
|-----|-------------|
| 7 | Visible flag (1 = displayed) |
| 6 | Enable attribute byte 4 |
| 5-0 | Sprite pattern number (0-63) |

If E=0: Sprite is an 8-bit anchor sprite using patterns 0-63
If E=1: Sprite is described by attribute byte 4

### Sprite Attribute 4

This byte has three different formats:

#### A. Extended Anchor Sprite

| Bit | Description |
|-----|-------------|
| 7 | H (1 = 4-bit pattern) |
| 6 | N6 (7th pattern bit for 4-bit patterns) |
| 5 | T (relative sprite type: 0=composite, 1=unified) |
| 4-3 | X magnification (00=1x, 01=2x, 10=4x, 11=8x) |
| 2-1 | Y magnification (00=1x, 01=2x, 10=4x, 11=8x) |
| 0 | Y8 (9th bit of Y coordinate) |

**Note**: {H,N6} must not equal {0,1} as this indicates a relative sprite.

#### B. Relative Sprite - Composite Type

| Bit | Description |
|-----|-------------|
| 7 | 0 (fixed) |
| 6 | 1 (fixed) |
| 5 | N6 (7th pattern bit for 4-bit patterns) |
| 4-3 | X magnification (00=1x, 01=2x, 10=4x, 11=8x) |
| 2-1 | Y magnification (00=1x, 01=2x, 10=4x, 11=8x) |
| 0 | PO (pattern offset relative to anchor) |

#### C. Relative Sprite - Unified Type

| Bit | Description |
|-----|-------------|
| 7 | 0 (fixed) |
| 6 | 1 (fixed) |
| 5 | N6 (7th pattern bit for 4-bit patterns) |
| 4-0 | Must be 0 except bit 0 |
| 0 | PO (pattern offset relative to anchor) |

## Relative Sprites

### 3.1 Composite Sprites

Composite sprites inherit from their anchor:
- Visibility (AND operation with anchor visibility)
- X/Y position (8-bit signed offset from anchor)
- Palette offset (if PR bit set)
- Pattern number (if PO bit set)
- 4-bit pattern flag

They act as independent sprites tied to an anchor.

### 3.2 Unified Sprites

Unified sprites inherit everything composite sprites do, plus:
- Rotation
- Mirroring  
- Scaling

They form a single large sprite controlled by the anchor, with automatic coordinate adjustments.

## Programming Sprites

### 4.1 I/O Ports

#### Sprite Status/Slot Select ($303B / 12347)

**Write Format**:

| Bit | Description |
|-----|-------------|
| 7 | X (unused) |
| 6-0 | Sprite/Pattern select number |

**Read Format**:

| Bit | Description |
|-----|-------------|
| 7-2 | Always 0 |
| 1 | M (max sprites per line exceeded) |
| 0 | C (sprite collision detected) |

#### Sprite Attribute Upload ($xx57 / 87) - Write Only

Writes sprite attributes sequentially after selecting via port $303B.

#### Sprite Pattern Upload ($xx5B / 91) - Write Only

Writes pattern data sequentially after selecting via port $303B.

### 4.2 Nextreg Interfaces

#### Register $34 (52) - Sprite Number

| Bit | Description |
|-----|-------------|
| 7 | Pattern address offset (if in lockstep mode) |
| 6-0 | Sprite number (0-127) |

Selects sprite for following attribute registers.

#### Register $35/$75 - Sprite Attribute 0

| Bit | Description |
|-----|-------------|
| 7-0 | X coordinate LSB |

Register $75 includes auto-increment of sprite number.

#### Register $36/$76 - Sprite Attribute 1

| Bit | Description |
|-----|-------------|
| 7-0 | Y coordinate LSB |

#### Register $37/$77 - Sprite Attribute 2

| Bit | Description |
|-----|-------------|
| 7-4 | Palette offset |
| 3 | X mirror |
| 2 | Y mirror |
| 1 | Rotate |
| 0 | X coordinate MSB |

#### Register $38/$78 - Sprite Attribute 3

| Bit | Description |
|-----|-------------|
| 7 | Visible flag |
| 6 | Extended attribute enable |
| 5-0 | Pattern number (0-63) |

#### Register $39/$79 - Sprite Attribute 4

| Bit | Description |
|-----|-------------|
| 7 | H (4-bit pattern flag) |
| 6 | N6 (pattern bit 6) |
| 5 | Relative sprite type |
| 4-3 | X scaling |
| 2-1 | Y scaling |
| 0 | Y coordinate MSB |

## 5. Global Control of Sprites

### Peripheral 4 Register ($09)

| Bit | Description |
|-----|-------------|
| 7 | AY 2 mono setting |
| 6 | AY 1 mono setting |
| 5 | AY 0 mono setting |
| 4 | Sprite ID lockstep |
| 3 | Disable Kempston port |
| 2 | Disable divMMC ports |
| 1-0 | Scanline intensity |

### Sprite and Layers System Register ($15)

| Bit | Description |
|-----|-------------|
| 7 | LoRes mode enable |
| 6 | Sprite priority |
| 5 | Enable sprite clipping |
| 4-2 | Layer priorities |
| 1 | Over border |
| 0 | Sprites visible |

### Clip Window Sprites Register ($19)

Defines sprite clipping window coordinates with four sequential writes:
1. X1 position
2. X2 position  
3. Y1 position
4. Y2 position

### Clip Window Control Register ($1C)

| Bit | Description |
|-----|-------------|
| 7-4 | Reserved (must be 0) |
| 3 | Reset tilemap clip index |
| 2 | Reset ULA/LoRes clip index |
| 1 | Reset sprite clip index |
| 0 | Reset Layer 2 clip index |

### Enhanced ULA Control Register ($43)

| Bit | Description |
|-----|-------------|
| 7 | Disable palette auto-increment |
| 6-4 | Select palette for read/write |
| 3 | Select sprites palette |
| 2 | Select Layer 2 palette |
| 1 | Select ULA palette |
| 0 | Enable ULANext mode |

### Palette Index Register ($40)

| Bit | Description |
|-----|-------------|
| 7-0 | Palette index selection |

### Palette Value Register ($41)

| Bit | Description |
|-----|-------------|
| 7-0 | Color value (RRRGGGBB format) |

### Enhanced ULA Palette Extension ($44)

Used for 9-bit color writes:

**First Write**:
| Bit | Description |
|-----|-------------|
| 7-0 | RRRGGGBB color bits |

**Second Write**:
| Bit | Description |
|-----|-------------|
| 7 | Priority flag (L2 palettes only) |
| 6-1 | Reserved (must be 0) |
| 0 | Blue LSB |

### Sprites Transparency Index Register ($4B)

| Bit | Description |
|-----|-------------|
| 7-0 | Transparency index value |

For 4-bit sprites, only bits 3-0 are used.
