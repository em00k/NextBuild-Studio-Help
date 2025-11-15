# DOTILE8 (DEPRECATED)

## Syntax

```
DoTile8(byVal X as ubyte, byval Y as ubyte, byval T as ubyte)
```

## Description

Draws a ``software`` 8x8pixel tile, starting from ``$c000`` on to Layer2 256x192 using 256 colours. The x and y coordinates are in a grid of `0-31` for x and `0-23` for y respectively.

### NOTICE 

This is a deprecated routine. Use [DoTileBank8](DoTileBank8.md) instead. This routine is still available for backwards compatibility, but is woefully inefficient due to the requirement of having to page in the tiles to ``$c000``, which will limit your available memory.

**Examples**

```	
dim tile as ubyte = 20 
dim bank as ubyte = 34
dim x, y as ubyte 
x = 10 : y = 10 

LoadSDBank("my8x8.spr",0,0,0,34) 	' Load tiles to bank 34
NextRegA($57,34)                    ' Set MMU7 $c000 to bank 34
DoTile8(x,y,tile)                   ' Draw tile 20 at 10,10 from $c000
NextRegA($57,1)                     ' Restore MMU7 $c000 to bank 1

```
[DoTile8](DoTile8.md)
[DoTileBank8](DoTileBank8.md)
[LoadSDBank](LoadSDBank.md)
[Graphics](_graphics.md)
