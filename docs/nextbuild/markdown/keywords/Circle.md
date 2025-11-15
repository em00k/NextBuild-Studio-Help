# CIRCLE

## Syntax

```
CIRCLE *x, y, radius*, CIRCLE *Attribute Modifiers*,*x, y, radius*
```

## Description

Draws a circle centered on coordinates (x, y) (see PLOT) with the given radius. Coordinate (0, 0) designates bottom-left screen corner. Drawing coordinates are updated to the last plotted position.
CIRCLE is enhanced in ZX BASIC to allow drawing on the last two screen rows (this was not possible in Sinclair BASIC). So now we have 16 lines more (192 in total). Sinclair BASIC only used top 176 scan lines. This means if in Sinclair BASIC you write:

	CIRCLE x,y,r

You must translate it to ZX BASIC as:

	CIRCLE x, y + 16, r

If you want both drawings to show at exactly the same vertical screen position. Also maximum circle radius size is 96, not 86.

Remarks

- his function is not strictly Sinclair BASIC compatible since it uses all 192 screen lines instead of top 176. If you translate ***PLOT***, ***DRAW*** & ***CIRCLE***, commands from Sinclair BASIC *as is* your drawing will be *shifted down* 16 pixels.
- This primitive uses Bresenham's algorithm for faster drawing instead of ROMs implementation.

More info : https://zxbasic.readthedocs.io/en/docs/circle/
