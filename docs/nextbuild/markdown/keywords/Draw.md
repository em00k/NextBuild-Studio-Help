# DRAW

## Syntax

```
DRAW dx, dy [, arc] OR  DRAW *Attribute Modifiers*; dx, dy [, arc]
```

## Description

Draws a straight line starting from the current drawing coordinates (x, y) (see PLOT) to (x + dx, y + dy) position. Coordinate (0, 0) designates bottom-left screen corner. Drawing coordinates are updated to the last position.

DRAW is enhanced in ZX BASIC to allow drawing on the last two screen rows (this was not possible in Sinclair BASIC). So now we have 16 lines more (192 in total). Sinclair BASIC only used top 176 scan lines. This means that in Sinclair BASIC

	PLOT x0, y0: DRAW x, y

is equivalent in ZX BASIC to

	PLOT x0, y0 + 16: DRAW x, y

**Remark This primitive uses Bresenham's algorithm for faster drawing instead of ROMs implementation.

**Drawing Arcs**

When used with 3 parameters it draws arcs the same way the Sinclair BASIC version does, but again the 192 scan-lines are available.

	DRAW dx, dy, arc

The above will draw an arc from the current position to (x + dx, y + dy) position, with a curve of ''arc'' radians. This routine also have some strange behaviors. High values of arc draws strange patterns.

**Remarks**
- This function is not strictly Sinclair BASIC compatible since it uses all 192 screen lines instead of top 176. If you translate **PLOT**, **DRAW** & **CIRCLE**, commands from Sinclair BASIC *as is* your drawing will be *shifted down* 16 pixels.

More info : https://zxbasic.readthedocs.io/en/docs/draw/
