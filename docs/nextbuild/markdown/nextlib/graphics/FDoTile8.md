# FDOTILE8

## Syntax

```
FDoTile8(tile id,x 0-39,y 0-31,bank)
```

## Description

Draws an ``software`` 8x8pixel tile from "bank" on to Layer2 320x256 in 256 colours. This routine will handle all paging requirements automatically. The x and y coordinates are in a grid of `0-39` for x and `0-31` for y respectively.

**Examples**

```
dim tile as ubyte = 20 
dim bank as ubyte = 34
dim x, y as ubyte 
x = 10 : y = 10 

LoadSDBank("my8x8.spr",0,0,0,34) 	' Load tiles to bank 34
FDoTile8(tile,x,y,bank) 			' Draw tile 20 at 10,10 from bank 34
```

[FDoTile16](FDoTile16.md)
[LoadSDBank](LoadSDBank.md)
[Graphics](_graphics.md)
