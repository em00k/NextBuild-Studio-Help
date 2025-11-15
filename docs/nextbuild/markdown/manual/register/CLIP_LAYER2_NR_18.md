# CLIP_LAYER2_NR_18

## Syntax

```
CLIP_LAYER2_NR_18 = $18
```

## Description

Register to set and read clip-window for Layer 2. (R\W)

The coordinates are stored under index:
```
Index	Coordinate
0	'X1 Position
1	'X2 Position
2	'Y1 Position
3	'Y2 Position
```

The current read/write index (which coordinate is selected) can be read or reset by Clip Window Control Register ($1C).

Write to register will modify currently selected coordinate, and auto-increment index (wrapping from 3 to 0).

Read from register will only read currently selected coordinate, index is not modified (to read next coordinate, write the current coordinate value back, to increment index).

The coordinate values are 0,255,0,191 after a Reset.

The displayed area is "inclusive", i.e. for default values full 256x192 pixel area is displayed.

## Remarks

More info : https://wiki.specnext.dev/Clip_Window_Layer_2_Register

```
#INCLUDE <nextlib.bas>
```

## Links 

[Index](Index.md)
