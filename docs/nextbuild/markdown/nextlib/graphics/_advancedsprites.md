# ZX Spectrum Next Sprite Programming Guide

## Table of Contents
- [ZX Spectrum Next Sprite Programming Guide](#zx-spectrum-next-sprite-programming-guide)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Notice](#notice)
  - [Sprite Coordinate System](#sprite-coordinate-system)
  - [Basic Sprite Setup](#basic-sprite-setup)
    - [Sprite Attributes Structure](#sprite-attributes-structure)
  - [Advanced Sprite Features](#advanced-sprite-features)
    - [Palette Offset](#palette-offset)
    - [Mirror and Rotate](#mirror-and-rotate)
    - [Scaling](#scaling)
  - [Big Sprites with Relative Sprites](#big-sprites-with-relative-sprites)
  - [Code Examples](#code-examples)
    - [Example 1: Basic Single Sprite](#example-1-basic-single-sprite)
    - [Example 2: Animated Sprite](#example-2-animated-sprite)
    - [Example 3: Big Sprite (2x2)](#example-3-big-sprite-2x2)
    - [Example 4: Composite Relative Sprites](#example-4-composite-relative-sprites)
    - [Example 5: Unified Big Sprite](#example-5-unified-big-sprite)
  - [Tips and Best Practices](#tips-and-best-practices)
  - [Common Patterns](#common-patterns)
    - [Moving Platform (4 sprites)](#moving-platform-4-sprites)
    - [Rotating Enemy](#rotating-enemy)

## Overview

## Notice 

This page is a work in progress. It is not complete and may contain errors. For now, please refer to [https://wiki.specnext.dev/Sprites](https://wiki.specnext.dev/Sprites) for more information.

The ZX Spectrum Next sprite system provides hardware-accelerated sprites with:
- 128 sprites total
- 16×16 pixel sprites (can be scaled 2x, 4x, or 8x)
- 8-bit (256 colors) or 4-bit (16 colors) patterns
- Hardware rotation, mirroring, and scaling
- Relative sprite system for complex objects

## Sprite Coordinate System

The sprite coordinate system uses 9-bit values (0-511) with wrap-around:
- **ULA Screen area**: Top-left at [32,32], bottom-right at [287,223]
- **Over-border area**: Full visible area is [0,0] to [319,255]
- **Wrap-around**: Position 511 acts as -1, 510 as -2, etc.

```
+---------------------------+
| Border (32px)             |
|   +-------------------+   |
|   | ULA Screen        |   |
|   | (256x192)         |   |
|   | [32,32]-[287,223] |   |
|   +-------------------+   |
| [0,0] to [319,255]        |
+---------------------------+
```

## Basic Sprite Setup

To display a sprite, you need to:
1. Upload a pattern to sprite pattern memory
2. Set sprite attributes (position, visibility, pattern)
3. Enable sprite display

### Sprite Attributes Structure

Each sprite has 4-5 attribute bytes:

| Byte | Description |
|------|-------------|
| 1 | X position (bits 0-7) |
| 2 | Y position (bits 0-7) |
| 3 | Palette offset, effects, X bit 8 |
| 4 | Visibility, pattern index, enable byte 5 |
| 5 | (Optional) Scale, sprite type, Y bit 8 |

## Advanced Sprite Features

### Palette Offset
- 4-bit value added to pattern color indices
- Allows recoloring sprites without changing patterns

### Mirror and Rotate
- X/Y mirroring for flipping sprites
- 90-degree clockwise rotation
- Applied in order: rotate, then mirror

### Scaling
- Independent X/Y scaling: 1x, 2x, 4x, 8x
- Reduces number of sprites per scanline when scaled

## Big Sprites with Relative Sprites

Two types of relative sprites:
1. **Composite**: Independent sprites positioned relative to anchor
2. **Unified**: Sprites that rotate/scale/mirror as one unit with anchor

## Code Examples

### Example 1: Basic Single Sprite

```asm
; Display a simple sprite at position [100, 80]

    ; First, enable sprites globally
    ld bc, $243B
    ld a, $15       ; Sprite and Layers System Register
    out (c), a
    ld bc, $253B
    ld a, %00000001 ; Enable sprites
    out (c), a

    ; Select sprite 0 for attribute upload
    ld bc, $303B
    ld a, 0
    out (c), a
    
    ; Upload sprite attributes via port $57
    ld bc, $57
    
    ; Byte 1: X position LSB
    ld a, 100
    out (c), a
    
    ; Byte 2: Y position LSB
    ld a, 80
    out (c), a
    
    ; Byte 3: Palette offset and effects
    ld a, %00000000  ; No palette offset, no effects, X bit 8 = 0
    out (c), a
    
    ; Byte 4: Visibility and pattern
    ld a, %10000001  ; Visible, no byte 5, pattern 1
    out (c), a
```

### Example 2: Animated Sprite

```asm
; Animate sprite by changing pattern index

    ; Select sprite 0
    ld bc, $303B
    ld a, 0
    out (c), a
    
    ; Keep position same, update pattern
    ld bc, $57
    
    ; Skip position bytes (auto-increment works)
    ld a, 100       ; X position
    out (c), a
    ld a, 80        ; Y position
    out (c), a
    ld a, 0         ; No effects
    out (c), a
    
    ; Update pattern for animation
    ld a, (frame_counter)
    and %00000111   ; Use patterns 0-7
    or %10000000    ; Keep visible
    out (c), a
```

### Example 3: Big Sprite (2x2)

```asm
; Create a 32x32 sprite using 4 sprites in a 2x2 pattern
; Using NextReg interface for clarity

    ; Sprite 0 - Top-left (anchor)
    NextReg $34, 0     ; Select sprite 0
    NextReg $35, 100   ; X position
    NextReg $36, 80    ; Y position
    NextReg $37, %00000000  ; No effects
    NextReg $38, %11000001  ; Visible, enable byte 5, pattern 1
    NextReg $39, %00010000  ; Anchor sprite, composite relatives, 2x scale

    ; Sprite 1 - Top-right (relative)
    NextReg $34, 1     ; Select sprite 1
    NextReg $35, 16    ; +16 pixels right (relative)
    NextReg $36, 0     ; Same Y as anchor (relative)
    NextReg $37, %00010000  ; Mirror X to use same pattern
    NextReg $38, %11000001  ; Visible, enable byte 5, same pattern
    NextReg $39, %01010001  ; Relative sprite, 2x scale, relative pattern

    ; Sprite 2 - Bottom-left (relative)
    NextReg $34, 2     ; Select sprite 2
    NextReg $35, 0     ; Same X as anchor (relative)
    NextReg $36, 16    ; +16 pixels down (relative)
    NextReg $37, %00100000  ; Mirror Y
    NextReg $38, %11000001  ; Visible, enable byte 5, same pattern
    NextReg $39, %01010001  ; Relative sprite, 2x scale, relative pattern

    ; Sprite 3 - Bottom-right (relative)
    NextReg $34, 3     ; Select sprite 3
    NextReg $35, 16    ; +16 right (relative)
    NextReg $36, 16    ; +16 down (relative)
    NextReg $37, %00110000  ; Mirror X and Y
    NextReg $38, %11000001  ; Visible, enable byte 5, same pattern
    NextReg $39, %01010001  ; Relative sprite, 2x scale, relative pattern
```

### Example 4: Composite Relative Sprites

```asm
; Create a spaceship with separate moving parts
; Main body (anchor) with turrets (relatives)

    ; Main ship body (anchor)
    NextReg $34, 10    ; Sprite 10
    NextReg $35, 160   ; Center screen X
    NextReg $36, 120   ; Center screen Y
    NextReg $37, %00100000  ; Palette offset 2
    NextReg $38, %11000101  ; Visible, enable byte 5, pattern 5
    NextReg $39, %00000000  ; Normal anchor, composite relatives

    ; Left turret (relative)
    NextReg $34, 11    ; Sprite 11
    NextReg $35, $F0   ; -16 pixels left (signed byte)
    NextReg $36, $F8   ; -8 pixels up
    NextReg $37, %00100000  ; Same palette as main
    NextReg $38, %11000110  ; Visible, pattern 6
    NextReg $39, %01000000  ; Composite relative
    
    ; Right turret (relative)  
    NextReg $34, 12    ; Sprite 12
    NextReg $35, 16    ; +16 pixels right
    NextReg $36, $F8   ; -8 pixels up
    NextReg $37, %00100000  ; Same palette
    NextReg $38, %11000110  ; Visible, pattern 6
    NextReg $39, %01000000  ; Composite relative
```

### Example 5: Unified Big Sprite

```asm
; Create a big sprite that rotates as one unit
; 2x2 sprite that maintains formation when rotated

    ; Anchor sprite with rotation
    NextReg $34, 20    ; Sprite 20
    NextReg $35, 150   ; X position
    NextReg $36, 100   ; Y position
    NextReg $37, %00000010  ; Enable rotation
    NextReg $38, %11000008  ; Visible, enable byte 5, pattern 8
    NextReg $39, %00100000  ; Anchor, unified relatives

    ; Top-right relative
    NextReg $34, 21    ; Sprite 21
    NextReg $35, 16    ; +16 right in local space
    NextReg $36, 0     ; Same Y in local space
    NextReg $37, %00000000  ; No local transform
    NextReg $38, %11000009  ; Pattern 9
    NextReg $39, %01000000  ; Unified relative

    ; Bottom-left relative
    NextReg $34, 22    ; Sprite 22
    NextReg $35, 0     ; Same X in local space
    NextReg $36, 16    ; +16 down in local space
    NextReg $37, %00000000  ; No local transform
    NextReg $38, %11000010  ; Pattern 10
    NextReg $39, %01000000  ; Unified relative

    ; Bottom-right relative
    NextReg $34, 23    ; Sprite 23
    NextReg $35, 16    ; +16 right in local space
    NextReg $36, 16    ; +16 down in local space
    NextReg $37, %00000000  ; No local transform
    NextReg $38, %11000011  ; Pattern 11
    NextReg $39, %01000000  ; Unified relative
```

## Tips and Best Practices

1. **Sprite Ordering**: Sprites are drawn in order 0-127. Use lower numbers for background sprites.

2. **Pattern Memory Management**: 
   - 8-bit patterns: 64 slots (256 bytes each)
   - 4-bit patterns: 128 slots (128 bytes each)

3. **Performance Considerations**:
   - Scaled sprites use more rendering time
   - Keep sprites on-screen to avoid wrap-around calculations
   - Use relative sprites to reduce attribute updates

4. **Animation Techniques**:
   - Change pattern index for frame animation
   - Use palette offset for color cycling
   - Combine rotation/mirror for more variations

5. **Debugging Tips**:
   - Start with simple static sprites
   - Use distinct colors/patterns to identify issues
   - Check sprite enable bit in register $15
   - Verify pattern upload before displaying sprite

## Common Patterns

### Moving Platform (4 sprites)
```asm
; Create a 64x16 platform using 4 sprites
platform_sprites:
    ; Leftmost section (anchor)
    db 32, 200      ; X, Y position
    db %00000000    ; No effects
    db %11000001    ; Visible, pattern 1
    
    ; Middle-left section
    db 16, 0        ; +16 relative X, same Y
    db %00000000    ; No effects  
    db %11000001    ; Same pattern
    db %01000001    ; Relative, use same pattern
    
    ; Middle-right section
    db 32, 0        ; +32 relative X
    db %00000000    ; No effects
    db %11000001    ; Same pattern  
    db %01000001    ; Relative
    
    ; Rightmost section
    db 48, 0        ; +48 relative X
    db %00000000    ; No effects
    db %11000001    ; Same pattern
    db %01000001    ; Relative
```

### Rotating Enemy
```asm
; Enemy that rotates while moving
update_enemy:
    ; Update position
    ld a, (enemy_x)
    inc a
    ld (enemy_x), a
    
    ; Set rotation based on frame
    ld a, (frame_counter)
    and %00000011   ; 0-3 for 4 rotation states
    rlca
    rlca            ; Shift to bits 2-1
    or %10000000    ; Add X mirror if needed
    
    ; Update sprite
    NextReg $34, 30
    NextReg $35, (enemy_x)
    NextReg $36, (enemy_y)
    NextReg $37, a   ; Rotation state
    NextReg $38, %11000100  ; Visible, pattern 4
```
* [Sprites](_sprites.md)
* [Graphics](_graphics.md)
* [NextReg](_nextreg.md)
