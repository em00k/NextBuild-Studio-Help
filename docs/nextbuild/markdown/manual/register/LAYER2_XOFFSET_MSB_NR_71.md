# LAYER2_XOFFSET_MSB_NR_71

## Syntax

```
LAYER2_XOFFSET_MSB_NR_71 = $71
```

## Description

**LAYER 2 X OFFSET MSB REGISTER** (R/W)

Sets the pixel offset used for drawing Layer 2 graphics on the screen. You can use [ScrollLayer2(x, y)](SCROLLLAYER2.md) for conveinience. 
```
bits 7-1 ' Reserved must be 0
bits 0   ' MSB scroll amount
```
This is most significant bit for high resolution **320x256x8** and **640x256x4** Layer 2 modes (valid range of scroll values is then [0..319], in **640x256x4** mode the layer is scrolling by two pixels horizontally)

The low 8 bits are defined by [Layer 2 X Offset Register $16](LAYER2_XOFFSET_LSB_NR_16.md)

## Links

More info : https://wiki.specnext.dev/Layer_2_X_Offset_MSB_Register

## Requires:
```
#INCLUDE <nextlib.bas>
```

[SCROLLLAYER](SCROLLLAYER.md)