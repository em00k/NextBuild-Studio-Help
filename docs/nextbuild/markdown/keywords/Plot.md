# PLOT

## Syntax

```
PLOT x,y, PLOT *Attribute Modifiers*; x, y
```

## Description

Plots a *pixel* at coordinates (x, y) (pixel column, pixel row). Coordinate (0, 0) designates bottom-left screen corner.

PLOT is enhanced in ZX BASIC to allow plotting in the last two screen rows (this was not possible in Sinclair BASIC). So now we have 16 lines more (192 in total). Sinclair BASIC only used top 176 scan-lines. This means that in Sinclair BASIC

	PLOT x, y

must be translated to ZX BASIC as

	PLOT x, y + 16

if you want your drawing to appear at the same vertical screen position Sinclair BASIC uses.

**Remarks**

- This function is not strictly Sinclair BASIC compatible since it uses all 192 screen lines instead of top 176. If you translate PLOT & DRAW commands from Sinclair BASIC as is your drawing will be shifted down 16 pixels.

More info : https://zxbasic.readthedocs.io/en/docs/plot/
