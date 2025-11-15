# CLIP_SPRITE_NR_19

## Syntax

```
CLIP_SPRITE_NR_19 = $19
```

## Description

**CLIP WINDOW SPRITES REGISTER** More info : https://wiki.specnext.dev/Clip_Window_Sprites_Register

Sets and reads clip-window for Sprites. (R\W)

The coordinates are stored under index:
```
Index	Coordinate
0	'X1 Position
1	'X2 Position
2	'Y1 Position
3	'Y2 Position
```
The current read/write index (which coordinate is selected) can be read or reset by **Clip Window Control Register** ($1C).

Write to register will modify currently selected coordinate, and auto-increment index (wrapping from 3 to 0).

Read from register will only read currently selected coordinate, index is not modified (to read next coordinate, write the current coordinate value back, to increment index).

**The coordinate values are 0,255,0,191 after a Reset.**

The displayed area is "inclusive", i.e. for default values full 256x192 pixel area is displayed.

Clip window on Sprites works by default only when the "draw over border" is disabled. With "over border" enabled, the clip window must be enabled extra by bit 5 in Sprite and Layers System Register ($15), and X-axis coordinates of clip-window are then doubled, see the Sprite and Layers System Register ($15) for details and example. Set it to {0,159,0,255} to cover whole pixel+border sprite area (320x256 pixels area of display) in the x-axis doubled mode. Although setting it larger (like {0,255,0,255}) should be safe operation and still the full 320x256 area for sprite pixels will be visible.

Requires: 
```
#INCLUDE <nextlib.bas>
```
 ## Links 

[Index](Index.md)
