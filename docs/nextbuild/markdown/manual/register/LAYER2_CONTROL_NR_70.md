# LAYER2_CONTROL_NR_70

## Syntax

```
LAYER2_CONTROL_NR_70 = $70
```

## Description

**LAYER 2 CONTROL REGISTER**

More info : https://wiki.specnext.dev/Layer_2_Control_Register

Layer 2 resolution, palette offset (R/W)

**Bits**

	7-6  'Reserved, must be 0
	5-4  'Layer 2 resolution (0 on reset)
		%00 ' 256x192x8bpp
		%01 ' 320x256x8bpp
		%10 ' 640x256x4bpp
	3-0  'Palette offset (soft reset = 0)

The 256x192x8bpp mode is simple 256 colour mode, one pixel is one byte (index into Layer 2 palette), pixels are stored from left to right, from top to bottom (next pixel to right is at +1 address, next pixel below is at +256 address), total memory is 48kiB = three 16kiB banks, starting at bank set in Layer 2 RAM Page Register ($12).

The 320x256x8bpp mode is similar, but pixels are stored from top to bottom, then from left to right! Next pixel to right is at +256 address, next pixel below is at +1 address (the image data are kind of "transposed" in memory). The clip window X coordinates are doubled like for tile mode and sprites. Total memory is 80kiB = five 16kiB banks, selected also by NextReg $12. The first bank then contains whole columns 0..63 (64 pixels width), the last fifth bank contains whole columns 256..319.

The 640x256x4bpp mode is more like 320x256x8bpp mode, but every byte is displayed as two half-width paired pixels, the left pixel colour extracted from top four bits %1111'0000, right pixel extracted from low four bits %0000'1111. This means that next two paired pixels below are at +1 address, and next two paired pixels at right are at +256 address.

Don't forget to set up the clip window for 320x256 or 640x256 modes, to make whole area visible, use 0,159,0,255 settings (the 640x256 does quadruple the value so X1=10,X2=80 makes pixels 40..323 visible (inclusive)). The Layer 2 clip window is by default set to 0,255,0,191 which shows full 256x192x8bpp mode, but it will make the larger modes appear cut at bottom.

Palette offset is added to top four bits of pixel value (in case of 4bpp mode it just forms top four bits of pixel value, nothing to add with, pixel data are bottom four bits) and does apply to all Layer 2 modes.

Requires: 

	#INCLUDE <nextlib.bas>
