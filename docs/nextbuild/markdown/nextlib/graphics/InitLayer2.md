# InitLayer2

## Syntax

```
InitLayer2(SCREEN_MODE)
```

## Description

Intialises Layer 2 in one of the following modes:

- MODE256X192
- MODE320X256
- MODE640X256

This command takes care of setting up the screen mode and clearing to colour 0 (usually black). 

**Examples**
```
#DEFINE LAYER2
#INCLUDE <nextlib.bas>
InitLayer2(MODE320X256)					' initialise 320 x 256 x 256 Colours
ShowLayer2(TRUE)					    ' enable Layer2
```

## Links

* [Layer2](_Layer2.md)
* [ShowLayer2](ShowLayer2.md)
