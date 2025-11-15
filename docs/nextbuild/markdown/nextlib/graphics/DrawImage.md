# DrawImage

## Syntax

```
DrawImage(byVal X as ubyte, byval Y as ubyte, @Image , frame as ubyte = 0)
```

## Description

Draws an image at x,y on Layer2 256x192. The image is a pointer to the image bank and dimensions. The frame is the frame to draw, which would work out to be (width * height) * frame into the image bank.

**Examples**

```	
; draw image at 10,10 from bank 32
dim x, y as ubyte 
x = 10 : y = 10 
DrawImage(x,y,@Image,0)


MyImage:
    asm 
        ; bank, width, height
        db 32, 10, 10
        ; offset in bank, if the image contains dimension as the first 2 bytes then you can omit the first 2 bytes
        ds 2
    end asm 
```
[DoTile8](DoTile8.md)
[DoTileBank8](DoTileBank8.md)
[LoadSDBank](LoadSDBank.md)
[Graphics](_graphics.md)
