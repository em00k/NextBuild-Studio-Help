# FDOTILE16

## Syntax

```
FDoTile16(tile id,x 0-19,y 0-15, bank)
```

## Description

Draws an ``software`` 16x16pixel tile from ``bank`` on to Layer2 320x256 in 256 colours. This routine will handle all paging requirements automatically. The x and y coordinates are in a grid of `0-19` for x and `0-15` for y respectively.

**Examples**

```
dim tile as ubyte = 20 
dim bank as ubyte = 34
dim x, y as ubyte 
x = 10 : y = 10 

LoadSDBank("my16x16.spr",0,0,0,34) 	' Load tiles to bank 34
FDoTile16(tile,x,y,bank) 			' Draw tile 20 at 10,10 from bank 34
```

[FDoTile8](FDoTile8.md)
[LoadSDBank](LoadSDBank.md)
[Graphics](_graphics.md)
