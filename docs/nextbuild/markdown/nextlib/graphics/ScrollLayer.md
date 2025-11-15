# ScrollLayer

## Syntax

```
ScrollLayer(x, y)
```

## Description

Scroll Layer 2 by x and y pixels. Valid values for x and y [0-255]. If you wish to scroll 

**Examples**
```
For x = 0 to 254
	ScrollLayer(x,0)				; Scroll screen right
	WaitRaster(192)					; wait for raster line 192
Next x
```

## Links

* [LAYER_2_X_OFFSET_REGISTER](LAYER_2_X_OFFSET_REGISTER.md)

* [NextRegister](NextRegister)
