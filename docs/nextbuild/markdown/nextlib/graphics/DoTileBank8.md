# DOTILEBANK8

## Syntax

```
DoTileBank8(x 0-31,y 0-23,tile id 0 - 255, bank)
```

## Description

Draws a ``software`` 8x8pixel tile, starting from ``bank`` on to Layer2 256x192 using 256 colours. This routine will handle all paging requirements automatically. The x and y coordinates are in a grid of `0-31` for x and `0-23` for y respectively. The maximum number of tiles is 256.

**Examples**

```	
dim tile as ubyte = 20 
dim bank as ubyte = 34
dim x, y as ubyte 
x = 10 : y = 10 

LoadSDBank("my8x8.spr",0,0,0,34) 	' Load tiles to bank 34
DoTileBank8(x,y,tile,bank) 		    ' Draw tile 20 at 10,10 from bank 34
```
[DoTile8](DoTile8.md)
[DoTileBank8](DoTileBank8.md)
[LoadSDBank](LoadSDBank.md)
[Graphics](_graphics.md)
