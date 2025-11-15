# Layer 2 Graphics

Layer 2 provides an additional high-resolution graphics layer that can display **256×192** or **320×256** pixels with **256 colors** each. This layer can appear above, below, or instead of the normal ULA screen.

Layer 2 is perfect for detailed graphics, smooth scrolling, and modern game visuals while keeping the classic Spectrum feel.

## Screen Modes

| Mode | Resolution | Colors | Memory |
|------|------------|--------|--------|
| Standard | 256×192 | 256 | 48KB (3 banks) |
| Extended | 320×256 | 256 | 80KB (5 banks) |
| High-res | 640×256 | 16 | 80KB (5 banks) |

## Basic Setup

**Enable Layer 2:**
```basic
' Enable Layer 2 for writing and set to 256x192 mode
InitLayer2(MODE256X192)
' Enable Layer 2 for writing and set to 320x256 mode
InitLayer2(MODE320X256)
' Enable Layer 2 for writing and set to 640x256 mode
InitLayer2(MODE640X256)
```

**Clear the screen:**
```basic
' Clear Layer 2 to black (color 0)
ClearLayer2(0)
```

## Drawing Pixels

In **256×192 mode**, pixels are stored in reading order (left to right, top to bottom):

```basic
' Example: Draw a red line
for x = 0 to 100
    PlotL2(x, 50, 255)  ' Color 255 = white
next x
```

## Quick Example

Here's a complete example that sets up Layer 2 and draws some graphics:

```basic
' Setup Layer 2
InitLayer2(MODE256X192)
ClearLayer2(0)  ' Clear to black

' Draw some colored squares
for i = 0 to 15
    FillRect(i * 16, i * 8, 16, 16, i + 1)
next i

' Show the layer
ShowLayer2(TRUE)

do : loop  ' Keep running

sub FillRect(x as ubyte, y as ubyte, w as ubyte, h as ubyte, color as ubyte)
    for py = y to y + h - 1
        for px = x to x + w - 1
            PlotL2(px, py, color)
        next px
    next py
end sub

```

## Scrolling

Layer 2 supports hardware scrolling for smooth movement:

```basic
' Scroll horizontally
NextReg(LAYER2_X_OFFSET_NR_16, offset_x)      ' X offset (0-255)
NextReg(LAYER2_X_OFFSET_MSB_NR_71, offset_x_msb)  ' X offset high bit

' Scroll vertically  
NextReg(LAYER2_Y_OFFSET_NR_17, offset_y)      ' Y offset (0-255)

' Example: Smooth horizontal scroll
for scroll = 0 to 255
    NextReg(LAYER2_X_OFFSET_NR_16, scroll)
    WaitRaster()  ' Wait for next frame
next scroll
```

## Layer Priority

Control which layer appears on top:

```basic
' Layer 2 above ULA
NextReg(SPRITE_CONTROL_NR_15, %000_000_10)

' Layer 2 below ULA 
NextReg(SPRITE_CONTROL_NR_15, %000_010_00)

' Layer 2 instead of ULA, sprites enable & over border  
NextReg(SPRITE_CONTROL_NR_15, %000_000_11)
```

## Palette

Layer 2 uses a 256-color palette that you can customize:

```basic
' Set palette color (0-255)
sub SetPaletteColor(index as ubyte, r as ubyte, g as ubyte, b as ubyte)
    dim c as ubyte 
    dim rr, gg, bb as ubyte 
    NextRegA(PALETTE_INDEX_NR_40, index)           ' Select palette index
    NextReg(PALETTE_CONTROL_NR_41, %00000000)       ' Layer 2 palette
    rr = r << 5
    gg=  g & $1f 
    bb=  b & $1f 
    ' rrrgggbb 
    c = r or g or b 
    NextRegA(PALETTE_VALUE_NR_41 c)               ' 
end sub

' Example: Set color 1 to bright red
SetPaletteColor(1, 255, 0, 0)
```

## Memory Layout

On a default Spectrum 128k, the Layer 2 memory is mapped to banks 9-11.

- **Banks 9-11** are used by default for 256×192 mode
- Each bank holds 64 lines of graphics
- **Bank 9**: Lines 0-63
- **Bank 10**: Lines 64-127  
- **Bank 11**: Lines 128-191

## Tips

- Always clear Layer 2 before drawing - it contains random data at startup
- Layer 2 pixels are in simple x,y order - no interlacing like ULA
- You can double-buffer by switching between different bank sets
- Avoid using banks 5, 7, and 8 for Layer 2 unless you know what you're doing

## Links

- [InitLayer2](InitLayer2.md)
- [ClearLayer2](ClearLayer2.md)
- [PlotL2](PlotL2.md)
- [InitPalette](InitPalette.md)

A complete example can be found in [NextBuild_Examples/Layer2Demo/main.bas](/NextBuild_Examples/Layer2Demo/main.bas) 