# L2Text(x,y,string,bank,colour mask)

## Syntax

```
L2Text(x, y, string, bank, colour mask)
```

## Description

Draws a string of text using a bitmap 8x8 256 colour font in `bank` on to Layer2 set to 256x192 mode. For 320x256 use [FL2Text()](FL2Text.md) instead.

**Example**

Load a font and print some text on Layer2 256x192
```
#INCLUDE <nextlib.bas> 
LoadSDBank("[]font3.spr",0,0,0,34) 			' load a font from the system assets into bank 34
L2Text(0,0,"HELLO NEXTBUILD",34)
DO : LOOP
```

**Remarks**

Note the use of [] in the filename, this tells the compiler to load the font from the system assets. There are around 1-25 fonts supplied in the system assets and can be loaded with [LoadSDBank()](LoadSDBank.md) and file names like `[]font3.spr`.

## Links

- [InitLayer2()](InitLayer2.md)
- [ShowLayer2()](ShowLayer2.md)
- [LoadSDBank()](LoadSDBank.md)


