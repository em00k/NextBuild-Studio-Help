# Circle2(x, y, radius, colour)

## Syntax

```
CircleL2(x [0-255], y [0-191], radius [0-255] , colour [0-255])
```

## Description

Draws a circle on Layer 2 with the specified colour. Currently this command will only work correctly with 256x192. 

**Example**

```
#INCLUDE <nextlib.bas>
InitLayer2(MODE256x192)
ClipLayer2(0,255,0,255)
WaitKey() : END 
```
**Remarks**

This command is a shortcut configuring [CLIP_LAYER2_NR_18](CLIP_LAYER2_NR_18) 4 times. 

Requires: 

```
#INCLUDE <nextlib.bas>
```

## Links 

[Index](Index.md)


