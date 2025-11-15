# DOTILEBANK16

## Syntax

```
DoTileBank16(x 0-19,y 0-15,tile id 0 - 255, bank)
```

## Description

Draws a ``software`` 16x16pixel tile, starting from ``bank`` on to Layer2 256x192 using 256 colours. This routine will handle all paging requirements automatically. The x and y coordinates are in a grid of `0-19` for x and `0-15` for y respectively. The maximum number of tiles is 256.

**Examples**


```	
dim tile as ubyte = 20 
dim bank as ubyte = 34
dim x, y as ubyte 
x = 10 : y = 10 

LoadSDBank("my16x16.spr",0,0,0,34) 	' Load tiles to bank 34
DoTileBank16(x,y,tile,bank) 		' Draw tile 20 at 10,10 from bank 34
```
[DoTile8](DoTile8.md)
[DoTileBank8](DoTileBank8.md)
[LoadSDBank](LoadSDBank.md)
[Graphics](_graphics.md)
