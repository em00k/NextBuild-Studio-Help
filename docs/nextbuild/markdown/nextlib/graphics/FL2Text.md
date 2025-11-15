# FL2Text(x,y,string,bank)

## Syntax

```
FL2Text(x, y, string, bank)
```

## Description

Draws a string of text using a bitmap 8x8 256 colour font in "bank" on to Layer2 set to 320x256 mode. For 256x192 use [L2Text()](L2Text.md) instead.

**Example**

Load a font and print some text on Layer2 320x256

```
InitLayer2(MODE320X256)		                ' set layer2 to 320x256 mode	
LoadSDBank("[]font3.spr",0,0,0,34) 			' load a font from the system assets into bank 34
FL2Text(0,0,"HELLO NEXTBUILD",34)
DO : LOOP
```

**Remarks**

Note the use of [] in the filename, this tells the compiler to load the font from the system assets. There are around 1-25 fonts supplied in the system assets and can be loaded with [LoadSDBank()](LoadSDBank.md) and file names like `[]font3.spr`.

## Links

- [L2Text()](L2Text.md)
- [LoadSDBank()](LoadSDBank.md)
- [NextReg()](NextReg.md)
- [NextRegA()](NextRegA.md)

