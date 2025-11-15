# Welcome to Nextbuild Studio

| Graphics   | Audio | Input/Output | FileIO | Hardware |
|:----------:|:-----:|:------------:|:------:|:--------:|
|[Layer2](_graphics.md)   | [SoundFX](_audio.md) | [Keyboard](_input.md) | [Load](_fileio.md) | [Registers](_registers.md) |
|[Sprites](_sprites.md)   | [Music](_audio.md)  | [Controllers](_input.md) | [Save](_fileio.md) | [Ports](_ports.md) |
|[TileMaps](_tilemaps.md)   | [Samples](_audio.md)  | [UART](_input.md) | [esxDOS](_esxdos.md)   | [Memory](_memory.md) |


- Quick link to : [Manual Pages](#manual-pages)
- Quick link to : [Syntax](syntax.md)
- Quick link to : [Keywords](_keywords.md)
- Quick link to : [Editors](EDITORS_INDEX.md)

## Table of Contents

- [Welcome to Nextbuild Studio](#welcome-to-nextbuild-studio)
  - [Table of Contents](#table-of-contents)
- [Welcome to NextBuild](#welcome-to-nextbuild)
  - [The Basics](#the-basics)
  - [Key Features](#key-features)
  - [Getting Started](#getting-started)
    - [Example: Hello World](#example-hello-world)
    - [Example: Drawing a Sprite](#example-drawing-a-sprite)
    - [Example: Simple Loop](#example-simple-loop)
  - [Basic Syntax](#basic-syntax)
  - [Useful Commands](#useful-commands)
  - [More Information](#more-information)
  - [Manual Pages](#manual-pages)

---

# Welcome to NextBuild

NextBuild is a modern, user-friendly programming environment designed for rapid development on the ZX Spectrum Next and compatible systems. It uses the flexible & powerful *[ZX Basic Compiler by Boriel](_zx_index.md)* enhanced with nextlib. It combines familiar BASIC-like syntax with powerful features for graphics, sound, and hardware control similar to AMOS.

ZX Basic Compiler is Copyleft (K) 2008-2025, Jose Rodriguez-Rosa (a.k.a. Boriel) https://zxbasic.readthedocs.io/en/docs/ The [Full Documention](_zx_index.md) is included along with v1.18.1 of the compiler in /NextBuildv9/zxbasic/.

## The Basics 

As NextBuild uses ZX Basic Compiler, it's best to familiarise yourself with the documentation, a good place to start is with the [**```Syntax Documentation```**](syntax.md). The help for the F1, and hover help all come from the project which you can find here [Boriel-Basic @ Github](https://github.com/boriel-basic/zxbasic). 

**IMPORTANT** The compiler has been tweaked for optimal operation with the ZX Spectrum Next - using a vanilla release may cause issues. 

## Key Features
- Simple, readable syntax
- Built-in support for sprites, tiles, and graphics
- Easy file and memory access
- Hardware and register access for advanced users
- Modern IDE integration with hover help and documentation

## Getting Started
A NextBuild program consists of statements and commands, much like traditional BASIC, but with enhancements for modern development.

### Example: Hello World

Create a new file, save it as "helloworld.bas", enter the following : 

```nextbuild
#INCLUDE <nextlib.bas>              ' Include the library
PRINT "Hello, NextBuild!"           ' Say HELLO!
WaitKey() : END                     ' Wait for keypress then reset
```

Now Press F6 - pick `Build Source & Run CSpect` and your program should say hello!

### Example: Drawing a Sprite
```nextbuild
#INCLUDE <nextlib.bas>
LoadSDBank("mysprites.spr",34)      ' Load sprites into RAM
InitSprites2(1,34)                  ' Upload to Sprite RAM 
SpritesOn(TRUE)                     ' Enable sprites 
UpdateSprite(100, 80, 1, 1, 0, 0)   ' Draw sprite #0 at (100,80) using pattern 1
WaitKey() : END 
```

**SPRITE SECTION** [Sprites](_Sprites.md)

### Example: Simple Loop

As NextBuild uses [ZX Basic Compiler](About.md) under the hood, it follows familiar ZX Spectrum BASIC syntax

```nextbuild
FOR I = 1 TO 10
    PRINT "Count: ", I
NEXT I
```

To access the ZX Spectrum Next hardware you will need to use the [*Registers*](_registers.md) name: 

Accessing Next Registers :
```
  NextReg($43, %00010000)  ; Pick first Layer2 Palette 
```
Or use the [*Register*](_registers.md) name: 
```
  NextReg(PALETTE_CONTROL_NR_43,%00010000)
```
Setting the CPU speed: 
```
  NextReg(TURBO_CONTROL_NR_07,%11)    ; %11 = 28Mhz
```
Drawing a tile:
```
 TBC
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

| Graphics | [Graphics](_graphics.md) |
| Sprites    | [Sprites](_sprites.md) |
| Audio     | [Audio](_audio.md) |
| File IO    | [File IO](_fileio.md) |
| Registers  | [Registers](_registers.md) |
| Constants | [Constants](_constants.md) | 
| Templates  | [Templates](_templates.md) |

Happy coding with NextBuild!
