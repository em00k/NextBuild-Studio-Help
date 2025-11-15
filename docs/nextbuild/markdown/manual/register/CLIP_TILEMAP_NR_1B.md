# CLIP_TILEMAP_NR_1B

## Syntax

```
CLIP_TILEMAP_NR_1B = $1B
```

## Description

**CLIP WINDOW TILEMAP REGISTER** More info : https://wiki.specnext.dev/Clip_Window_Tilemap_Register

Sets and reads clip-window for Tilemap. (R\W)

The coordinates are stored under index:

```
Index	Coordinate
0	'X1 Position
1	'X2 Position
2	'Y1 Position
3	'Y2 Position
```

The current read/write index (which coordinate is selected) can be read or reset by Clip Window Control Register ($1C).

Write to register will modify currently selected coordinate, and auto-increment index (wrapping from 3 to 0).

Read from register will only read currently selected coordinate, index is not modified (to read next coordinate, write the current coordinate value back, to increment index).

The X coordinates are internally doubled (40x32 mode) or quadrupled (80x32 mode), and origin [0,0] is 32* pixels left and above the top-left ULA pixel, i.e. Tilemap mode does use same coordinates as Sprites, reaching 32* pixels into "BORDER" on each side.

**The coordinate values are 0,159,0,255 after a Reset.**

The displayed area is "inclusive", i.e. for default values full 320x256 (640x256) sprite-pixel area is displayed.

*32 pixels in 40x32 mode, when pixels have identical width with classic ULA and Sprite pixels. In 80x32 mode the pixels have half width, but they cover the identical screen area, so the first ULA pixel is then at [64,32] position out of [0..639,0..255] area.  

Requires: 
```
#INCLUDE <nextlib.bas>
```

## Links 

[Index](Index.md)
