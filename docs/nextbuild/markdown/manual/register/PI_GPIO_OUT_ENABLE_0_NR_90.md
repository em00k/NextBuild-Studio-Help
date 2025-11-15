# PI_GPIO_OUT_ENABLE_0_NR_90

## Syntax

```
PI_GPIO_OUT_ENABLE_0_NR_90 = $90
```

## Description

**PI GPIO OUTPUT ENABLE REGISTER** (R/W)

More info : https://wiki.specnext.dev/Pi_GPIO_Output_Enable_Register

-  Bits 27-0: Set bits enable GPIO output on the corresponding GPIO pin (soft reset = all 0)

GPIO pins 1:0 cannot be enabled.

The register $93 is MSB (most significant byte = bits 31-24), register $90 is LSB (least significant byte = bits 7-0).

Bits 31-28 are not explicitly specified in the docs, so consider them "Reserved, preserve current value".

(note: Next registers with number higher than $7F are inaccessible from Copper code) 

Requires: 

	#INCLUDE <nextlib.bas>
