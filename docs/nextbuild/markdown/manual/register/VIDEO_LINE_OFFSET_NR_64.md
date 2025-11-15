# VIDEO_LINE_OFFSET_NR_64

## Syntax

```
VIDEO_LINE_OFFSET_NR_64 = $64
```

## Description

**VERTICAL VIDEO LINE OFFSET REGISTER** (R/W)

More info : https://wiki.specnext.dev/Vertical_Video_Line_Offset_Register

Offset numbering of raster lines in copper/interrupt/active register

Bits 7-0 form offset value 0..255, the offset is added to Copper, Video Line Interrupt and Active Video Line readings.

Normally the ULA's pixel row 0 aligns with vertical line count 0. With a non-zero offset, the ULA's pixel row 0 will align with the vertical line offset.

Eg, if the offset is 32 then video line 32 will correspond to the first pixel row in the ULA and video line 0 will align with the first pixel row of the Tilemap and Sprites (in the top border area). Then Copper WAIT command waiting for line 0 will happen already in top border area.

Also Copper mode %11 restarting CPC=0 at pixel [0,0] (with offset 0) will be offset to new line!

Since a change in offset takes effect when the ULA reaches row 0, the change can take up to one frame to occur.

(also related: Active Video Line MSB Register ($1E), Active Video Line LSB Register ($1F), Video Line Interrupt Control Register ($22), Video Line Interrupt Value Register ($23) and Copper)  

Requires: 

	#INCLUDE <nextlib.bas>
