# NextBuild Manual

## Sprites
- [Introduction](#Sprites-Introduction)
- [Loading Sprites](#loading-sprites)
- [Display Sprites](#display-sprites)
- [Example](#example-1)
- [In Depth](#in-depth)
- [NextBuild Sprite Editor](sprite_editor)
---

# Sprites Introduction

The ZX Spectrum Next supports up to 128 hardware sprites on screen at anyone time with 64 different images `patterns` in 8-bit mode or 128 `patterns` in 4-bit mode. 

Sprites can be place anywhere on screen including over the border. They can be extruded X/Y by x2 x4 or x8. Sprites can be mirrored, rotated or flipped. Sprites are a very power resource and using them inside NextBuild could not be simpler.

## Key Features
- 16x16 pixels in size 
- 128 sprites on screen (max 12 per scanline)
- 64 or 128 different `patterns`
- 256 colour 8-bit mode or 16 colour 4-bit mode 
- 
- Appear on top, middle or bottom of the layer system 



## Loading Sprites 

A NextBuild program consists of statements and commands, much like traditional BASIC, but with enhancements for modern development.

### Example: Hello World
```nextbuild
#INCLUDE <nextlib.bas>              ' Include the library
PRINT "Hello, NextBuild!"           ' Say HELLO!
WaitKey() : END                     ' Wait for keypress then reset
```

### Example: Drawing a Sprite
```nextbuild
#INCLUDE <nextlib.bas>
ShowSprites(0)                      ' Hide all sprites 
LoadSDBank("mysprites.spr",34)      ' Load sprites into RAM
InitSprites2(1,34)                  ' Upload to Sprite RAM 
UpdateSprite(100, 80, 1, 1, 0, 0)   ' Draw sprite #0 at (100,80) using pattern 1
ShowSprites(1)                      ' Show all sprites 
WaitKey() : END 
```


### Example: Simple Loop

As NextBuild uses ZX Basic Compiler under the hoot it follows familiar ZX Spectrum BASIC syntax

```nextbuild
FOR I = 1 TO 10
    PRINT "Count: ", I
NEXT I
```

## Basic Syntax
- Statements are written one per line
- Comments start with `'` or `REM`
- Variables are automatically typed
- Use `LET` for assignment (optional)

## Useful Commands
- `NextReg(R,N)`        - Set Next register R with value N
- `PRINT`               - Output text to the screen
- `InitLayer2(MODE)`    - Set up Layer2 
- `UpdateSprite()`      - Draw or move a sprite
- `PALETTE`             - Set color palette
- `PEEK`/`POKE`         - Read/write memory

## More Information
- Use the F1 key or hover over keywords in the editor for instant help.
- Explore the manual pages for details on graphics, sound, and advanced features.

## Manual Pages
- [Sprites](sprites.md)
- [Layer2](layer2.md)
- [Registers](registers.md)
- [File IO](fileio.md)
- [Audio](audio.md)
- [Constants](constants.md)

Happy coding with NextBuild!
