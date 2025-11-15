# LORES_YOFFSET_NR_33

## Syntax

```
LORES_YOFFSET_NR_33 = $33
```

## Description

**LORES Y OFFSET REGISTER**

More info : https://wiki.specnext.dev/LoRes_Y_Offset_Register

Pixel Y offset (0..191) to use when drawing LoRes Layer.

bits 7-0 = Y Offset (0-191) (Reset to 0 after a reset)

LoRes scrolls in "half-pixels" at the same resolution and smoothness as Layer 2 (0-191).

Requires: 

	#INCLUDE <nextlib.bas>
