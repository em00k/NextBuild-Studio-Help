# NextBuild Quick Reference

This is a reference-only page that will appear in the help system but not in hover help or autocomplete.

## Syntax Quick Reference

### Control Structures
```nextbuild
IF condition THEN
    statements
ELSEIF condition THEN
    statements
ELSE
    statements
END IF

FOR i = start TO end [STEP step]
    statements
NEXT [i]

DO [WHILE|UNTIL condition]
    statements
LOOP [WHILE|UNTIL condition]

WHILE condition
    statements
WEND

```

### Common NextBuild Commands

#### Graphics
- `InitLayer2(MODE256X192)` - Initialize Layer 2 graphics
- `ShowLayer2(visible)` - Show/hide Layer 2
- `PlotL2(x, y, color)` - Plot a pixel on Layer 2
- `InitSprites2(number of sprites, address ,bank)` - Initialize sprites from a bank 
- `UpdateSprite(x, y, pattern, frame, rot, mirror)` - Draw sprite see [Sprites](sprites.md)

#### Input/Output
- `WaitKey()` - Wait for key press
- `Inkey$()` - Get current key press as string
- `Print "text"` - Output text to screen
- `NextReg(r, v)` - Write to Next register

#### File Operations
- `LoadSDBank(filename, bank)` - Load file to RAM bank
- `SaveSDBank(filename, bank, length)` - Save RAM bank to file

### Useful Constants
- `TRUE` = -1
- `FALSE` = 0
- `NULL` = 0
- `PI` = 3.14159265359

[Back to Index](index.md#welcome-to-nextbuild) 